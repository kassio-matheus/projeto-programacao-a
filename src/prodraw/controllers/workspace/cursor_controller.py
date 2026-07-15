from tkinter import Event, StringVar
from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Callable
import random


from prodraw.models.workspace.cursor_model import CursorModel
from prodraw.views.workspace.cursor_view import CursorView
from prodraw.controllers.shapes.tools import Tools

# Shapes controllers
from prodraw.controllers.shapes.rectangle import rectangle_sync_data
from prodraw.controllers.shapes.oval import oval_sync_data
from prodraw.controllers.shapes.square import square_sync_data
from prodraw.controllers.shapes.circle import circle_sync_data
from prodraw.controllers.shapes.line import line_sync_data
from prodraw.controllers.shapes.freedraw import freedraw_sync_data

# Color mappings
SHAPE_COLORS = {
    "#FFFFFF": "#2C3036",
    "#9398B0": "#2C3036",
    "#E599F7": "#383442",
    "#AE3EC9": "#352938",
    "#4F72FC": "#262E40",
    "#4DABF7": "#2A3642",
    "#FFC034": "#3B352B",
    "#F76710": "#3B2E27",
    "#0B9268": "#263231",
    "#40C057": "#293830",
    "#FF8787": "#3C2B2B",
    "#E03131": "#382727"
}

WORKSPACE_COLORS = {
    "bg": '#101010'
}


@dataclass
class CursorController(Tools):
    """
    Bridges raw Tkinter mouse events and the Cursor model/view.
    This is the only layer allowed to know about both Tkinter events
    and business rules (model state).
    """
    current: CursorModel = None
    is_selected: bool = False
    selected_figures: List[Tuple[str, int]] = field(default_factory=list)

    # Dictionary to store the original style of shapes.
    # Using a dict prevents duplicate entries and style overwriting bugs.
    changed_figures: Dict[int, dict] = field(default_factory=dict)

    # List to store copied's shapes
    copied_figures: List[Tuple[str, int]] = field(default_factory=list)

    # Flag to track whether the selected figure was moved (dragged) after the click.
    has_moved: bool = False

    # Keep track of the last mouse position to calculate real-time dx, dy
    last_x: float = 0.0
    last_y: float = 0.0

    # Reference to the selected color StringVar from workspace.py
    selected_color_var: StringVar = None

    def _get_figure_by_model_id(self, target_id_str: str) -> Tuple[str, int]:
        """Find the shape_type and index in the data based on the 'id_...' tag."""
        for shape_type, shape_list in self.figures.items():
            for index, shape in enumerate(shape_list):
                if isinstance(shape, dict):
                    model_id = shape.get('shape_id')
                else:
                    model_id = shape[0]

                if str(model_id) == target_id_str:
                    return (shape_type, index)
        return None

    def _get_selected_figures(self, sx0: float, sy0: float, sx1: float, sy1: float) -> List[Tuple[str, int]]:
        """Helper method to find all shapes within a specific bounding box."""
        selected = []
        sel_min_x, sel_max_x = min(sx0, sx1), max(sx0, sx1)
        sel_min_y, sel_max_y = min(sy0, sy1), max(sy0, sy1)

        for shape_type, shape_list in self.figures.items():
            for index, shape in enumerate(shape_list):
                if shape_type in ('Rectangle', 'Oval', 'Square', 'Line'):
                    fx0, fy0, fx1, fy1 = shape[1], shape[2], shape[3], shape[4]
                    fig_min_x, fig_max_x = min(fx0, fx1), max(fx0, fx1)
                    fig_min_y, fig_max_y = min(fy0, fy1), max(fy0, fy1)

                elif shape_type == 'Circle':
                    cx, cy, r = shape[1], shape[2], shape[3]
                    fig_min_x, fig_max_x = cx - r, cx + r
                    fig_min_y, fig_max_y = cy - r, cy + r

                elif shape_type == 'FreeDraw':
                    positions = shape['positions']
                    if not positions:
                        continue
                    xs = [p[0] for p in positions]
                    ys = [p[1] for p in positions]
                    fig_min_x, fig_max_x = min(xs), max(xs)
                    fig_min_y, fig_max_y = min(ys), max(ys)
                else:
                    continue

                if (fig_min_x <= sel_max_x and fig_max_x >= sel_min_x and
                        fig_min_y <= sel_max_y and fig_max_y >= sel_min_y):
                    selected.append((shape_type, index))

        return selected

    def _get_selected_shape_ids(self) -> List[int]:
        """
        Resolves the canvas shape_id (the number used in the "id_<shape_id>"
        tag) for every figure currently listed in self.selected_figures.
        """
        shape_ids = []

        for shape_type, index in self.selected_figures:
            try:
                shape = self.figures[shape_type][index]
            except IndexError:
                continue

            if isinstance(shape, dict):
                shape_id = shape.get('shape_id')
            else:
                shape_id = shape[0]

            if shape_id is not None:
                shape_ids.append(shape_id)

        return shape_ids

    def _get_figure_stack(self) -> List[int]:
        """
        Returns the shape_id of every figure currently drawn on the canvas,
        ordered bottom -> top according to the real Tkinter stacking order.

        Non-figure items (grid dots, logo, etc.) are ignored since they don't
        carry an "id_<shape_id>" tag — the same convention already used in
        _on_press, _select_figure_update_style and delete_selected_figures.
        """
        stack = []
        seen = set()

        for item_id in self.canvas.find_all():
            for tag in self.canvas.gettags(item_id):
                if tag.startswith("id_"):
                    shape_id = int(tag[3:])
                    if shape_id not in seen:
                        seen.add(shape_id)
                        stack.append(shape_id)
                    break

        return stack

    def _move_figure(self, shape_type: str, index: int, dx: float, dy: float):
        """
        Move a shape by (dx, dy).
        Updates the internal model and visually moves it on the Tkinter canvas.
        """
        shape = self.figures[shape_type][index]

        if shape_type in ('Rectangle', 'Oval'):
            shape_id, x0, y0, x1, y1, w, h, color = shape
            self.figures[shape_type][index] = (
                shape_id, x0 + dx, y0 + dy, x1 + dx, y1 + dy, w, h, color)

        elif shape_type == 'Square':
            shape_id, x0, y0, x1, y1, size, color = shape
            self.figures[shape_type][index] = (
                shape_id, x0 + dx, y0 + dy, x1 + dx, y1 + dy, size, color)

        elif shape_type == 'Line':
            shape_id, x0, y0, x1, y1, length, color = shape
            self.figures[shape_type][index] = (
                shape_id, x0 + dx, y0 + dy, x1 + dx, y1 + dy, length, color)

        elif shape_type == 'Circle':
            shape_id, cx, cy, r, color = shape
            self.figures[shape_type][index] = (
                shape_id, cx + dx, cy + dy, r, color)

        elif shape_type == 'FreeDraw':
            new_positions = [(x + dx, y + dy) for x, y in shape['positions']]
            self.figures[shape_type][index]['positions'] = new_positions

        if isinstance(shape, dict):
            canvas_id = shape.get('shape_id')
        else:
            canvas_id = shape[0]

        if canvas_id is not None:
            self.canvas.move(f"id_{canvas_id}", dx, dy)

    def _select_figure_update_style(self, shape_id: int, isSelected: bool = True):
        """
        Updates the style of the figure to indicate selection.
        Ensures the original style is safely stored and restored.
        Selection is always the inverse of the original style (dotted -> solid, solid -> dotted).
        """
        if isSelected:
            self._sync_tool_options_to_selected_shape(shape_id)

            # Only save the original style if the shape_id is not already in the dictionary.
            if shape_id not in self.changed_figures:
                raw_shape_config = self.canvas.itemconfig(f"id_{shape_id}")
                old_shape_style = {key: value[-1]
                                   for key, value in raw_shape_config.items()}
                self.changed_figures[shape_id] = old_shape_style

            shape_type = self.canvas.type(f"id_{shape_id}")

            # Detect if the original border was dotted/dashed
            original_dash = self.changed_figures[shape_id].get("dash", "")
            is_dotted = False
            if original_dash:
                if isinstance(original_dash, (list, tuple)) and len(original_dash) > 0:
                    is_dotted = True
                elif isinstance(original_dash, str) and original_dash.strip() not in ("", "0"):
                    is_dotted = True

            selection_color = "#5B5B5B"

            if (shape_type != "line"):
                # If original is dotted, selection is SOLID. Otherwise selection is DOTTED.
                target_dash = "" if is_dotted else (4, 4)
                self.canvas.itemconfig(
                    f"id_{shape_id}", outline=selection_color, dash=target_dash)
            else:
                # If original is dotted, selection is SOLID. Otherwise selection is DOTTED.
                target_dash = "" if is_dotted else (6, 6)
                self.canvas.itemconfig(
                    f"id_{shape_id}", fill=selection_color, dash=target_dash)
        else:
            # Restore the original style and safely remove it from the dictionary using pop()
            shape_style = self.changed_figures.pop(shape_id, None)

            if shape_style:
                self.canvas.itemconfig(f"id_{shape_id}", **shape_style)

    def change_shape_color(self, bg_color: str, outline_color: str, shape_id: int = None):
        """
        Public method to change both the background (fill) and border (outline) colors of shapes.
        Resolves correct high/low contrast styles using SHAPE_COLORS.
        """
        # Resolve correct high-contrast border and low-contrast fill colors
        if outline_color in SHAPE_COLORS:
            border_color = outline_color
            fill_color = SHAPE_COLORS[outline_color]
        elif bg_color in SHAPE_COLORS:
            border_color = bg_color
            fill_color = SHAPE_COLORS[bg_color]
        else:
            border_color = outline_color
            fill_color = bg_color

        # 1. Determine target figures to update
        targets = []
        if shape_id is not None:
            found_info = self._get_figure_by_model_id(str(shape_id))
            if found_info:
                targets.append(found_info)
        else:
            targets = list(self.selected_figures)

        # 2. Apply color updates to all targeted shapes
        for shape_type, index in targets:
            try:
                shape = self.figures[shape_type][index]
            except IndexError:
                continue

            if isinstance(shape, dict):
                current_id = shape.get('shape_id')
            else:
                current_id = shape[0]

            if current_id is None:
                continue

            # 3. Synchronize internal model using border_color as reference
            if shape_type in ('Rectangle', 'Oval'):
                _, x0, y0, x1, y1, w, h, _ = shape
                self.figures[shape_type][index] = (
                    current_id, x0, y0, x1, y1, w, h, border_color
                )

            elif shape_type == 'Square':
                _, x0, y0, x1, y1, size, _ = shape
                self.figures[shape_type][index] = (
                    current_id, x0, y0, x1, y1, size, border_color
                )

            elif shape_type == 'Line':
                _, x0, y0, x1, y1, length, _ = shape
                self.figures[shape_type][index] = (
                    current_id, x0, y0, x1, y1, length, border_color
                )

            elif shape_type == 'Circle':
                _, cx, cy, r, _ = shape
                self.figures[shape_type][index] = (
                    current_id, cx, cy, r, border_color
                )

            elif shape_type == 'FreeDraw':
                if isinstance(shape, dict):
                    self.figures[shape_type][index]['color'] = border_color

            # 4. Visually update canvas and selection style cache
            if current_id in self.changed_figures:
                original_style = self.changed_figures[current_id]

                was_filled = original_style.get("fill", "") != ""
                was_bordered = original_style.get("outline", "") != ""

                if shape_type != 'Line' and shape_type != 'FreeDraw':
                    # If shape has solid fill but no border, apply the strong color as fill
                    if was_filled and not was_bordered:
                        original_style['fill'] = border_color
                        original_style['outline'] = ""
                    else:
                        original_style['fill'] = fill_color if was_filled else ""
                        original_style['outline'] = border_color if was_bordered else ""

                    self.canvas.itemconfig(
                        f"id_{current_id}", fill=original_style['fill'])
                else:
                    original_style['fill'] = border_color
                    self.canvas.itemconfig(
                        f"id_{current_id}", fill=border_color)
            else:
                if shape_type == 'Line' or shape_type == 'FreeDraw':
                    self.canvas.itemconfig(
                        f"id_{current_id}", fill=border_color)
                else:
                    has_fill = self.canvas.itemcget(
                        f"id_{current_id}", "fill") != ""
                    has_outline = self.canvas.itemcget(
                        f"id_{current_id}", "outline") != ""

                    # If shape has solid fill but no border, apply the strong color as fill
                    if has_fill and not has_outline:
                        target_fill = border_color
                        target_outline = ""
                    else:
                        target_fill = fill_color if has_fill else ""
                        target_outline = border_color if has_outline else ""

                    if not has_fill and not has_outline:
                        target_fill = fill_color
                        target_outline = border_color

                    self.canvas.itemconfig(
                        f"id_{current_id}", fill=target_fill, outline=target_outline)

    def update_tool_options_state(self):
        """Updates the Tool Options panel state based on the current selection list."""
        if not hasattr(self, 'tool_options_controller') or not self.tool_options_controller:
            return

        # If nothing is selected, reactivate the panel with default model options
        if not self.selected_figures:
            current_fill = self.tool_options_controller.model.get_fill()
            current_border = self.tool_options_controller.model.get_border()
            self.tool_options_controller.sync_ui_from_shape(
                current_fill, current_border, is_disabled=False)
            # self.update_tool_options_state()

            return

        # Synchronize based on the last selected shape in list
        last_shape_type, last_index = self.selected_figures[-1]
        try:
            shape = self.figures[last_shape_type][last_index]
            if isinstance(shape, dict):
                current_id = shape.get('shape_id')
            else:
                current_id = shape[0]

            if current_id is not None:
                self._sync_tool_options_to_selected_shape(current_id)
        except IndexError:
            pass

    def update_shape_style(self, option_id: str, category: str, active_color: str = None):
        """
        Updates the style (fill options or border dash) of selected shapes.
        """
        if not self.selected_figures:
            return

        if active_color:
            active_border_color = active_color
        else:
            # Fallback to white if no color var is found
            active_border_color = self.selected_color_var.get() if hasattr(
                self, 'selected_color_var') and self.selected_color_var else "#FFFFFF"

        # Try to fetch the contrasting fill color
        try:
            active_fill_color = SHAPE_COLORS.get(
                active_border_color, "#2C3036")
        except NameError:
            active_fill_color = "#2C3036"  # Fallback neutral dark gray

        for shape_type, index in self.selected_figures:
            try:
                shape = self.figures[shape_type][index]
                if isinstance(shape, dict):
                    current_id = shape.get('shape_id')
                else:
                    current_id = shape[0]

                if current_id is None:
                    continue

                tk_type = self.canvas.type(f"id_{current_id}")

                if current_id in self.changed_figures:
                    original_style = self.changed_figures[current_id]

                    if category == "fill" and tk_type != "line":
                        if option_id == "solid_border":
                            original_style["fill"] = active_fill_color
                            original_style["outline"] = active_border_color
                            original_style["width"] = 1.5
                        elif option_id == "solid_no_border":
                            original_style["fill"] = active_border_color
                            original_style["outline"] = ""
                            original_style["width"] = 1.5
                        elif option_id == "no_solid_border":
                            original_style["fill"] = ""
                            original_style["outline"] = active_border_color
                            original_style["width"] = 3.5

                        self.canvas.itemconfig(
                            f"id_{current_id}",
                            fill=original_style["fill"],
                            width=original_style["width"],
                            outline=original_style["outline"]
                        )

                    elif category == "border":
                        if option_id == "solid":
                            original_style["dash"] = ""
                            if tk_type != "line":
                                if original_style.get("outline", "") == "":
                                    original_style["outline"] = active_border_color
                            else:
                                original_style["fill"] = active_border_color

                        elif option_id == "dotted":
                            original_style["dash"] = (6, 6)

                            if tk_type != "line":
                                if original_style.get("outline", "") == "":
                                    original_style["outline"] = active_border_color
                            else:
                                original_style["fill"] = active_border_color

                        if tk_type != "line":
                            self.canvas.itemconfig(
                                f"id_{current_id}",
                                dash=original_style["dash"],
                                outline=original_style.get(
                                    "outline", active_border_color)
                            )
                        else:
                            self.canvas.itemconfig(
                                f"id_{current_id}",
                                dash=original_style["dash"],
                                fill=original_style.get(
                                    "fill", active_border_color)
                            )

            except IndexError:
                continue

    def copy_shapes(self, event: Event = None):
        self.copied_figures = self.selected_figures

    def paste_shapes(self, event: Event = None):
        # Distance in pixels on paste the duplicated shape
        distance = random.randint(20, 50)

        for figure in self.copied_figures:
            shape_type = figure[0]
            index = figure[1]

            shape = self.figures[shape_type][index]

            if shape_type == 'Rectangle':
                shape_id, start_x, start_y, end_x, end_y, distance_x, distance_y, bg = shape
                duplicated_shape = random.randint(1, 10000000), start_x + distance, start_y + \
                    distance, end_x + distance, end_y + distance, distance_x, distance_y, bg

                rectangle_sync_data(canvas=self.canvas,
                                    figures=self.figures, data=duplicated_shape)

                self.figures['Rectangle'].append(duplicated_shape)

            elif shape_type == 'Oval':
                shape_id, start_x, start_y, end_x, end_y, distance_x, distance_y, bg = shape
                duplicated_shape = random.randint(1, 10000000), start_x + distance, start_y + \
                    distance, end_x + distance, end_y + distance, distance_x, distance_y, bg

                oval_sync_data(canvas=self.canvas,
                               figures=self.figures, data=duplicated_shape)

                self.figures['Oval'].append(duplicated_shape)

            elif shape_type == 'Square':
                shape_id, start_x, start_y, end_x, end_y, distance_x, bg = shape
                duplicated_shape = random.randint(1, 10000000), start_x + distance, start_y + \
                    distance, end_x + distance, end_y + distance, distance_x, bg

                square_sync_data(canvas=self.canvas,
                                 figures=self.figures, data=duplicated_shape)

                self.figures['Square'].append(duplicated_shape)

            elif shape_type == 'Line':
                shape_id, start_x, start_y, end_x, end_y, distance_x, bg = shape
                duplicated_shape = random.randint(1, 10000000), start_x + distance, start_y + \
                    distance, end_x + distance, end_y + distance, distance_x, bg

                line_sync_data(canvas=self.canvas,
                               figures=self.figures, data=duplicated_shape)

                self.figures['Line'].append(duplicated_shape)

            elif shape_type == 'Circle':
                shape_id, x, y, radius, bg = shape
                duplicated_shape = random.randint(1, 10000000), x + distance, y + \
                    distance, radius, bg

                circle_sync_data(canvas=self.canvas,
                                 figures=self.figures, data=duplicated_shape)

                self.figures['Circle'].append(duplicated_shape)

            elif shape_type == 'FreeDraw':
                if isinstance(shape, dict):
                    pass

    def delete_selected_figures(self, event: Event = None):
        """
        Public method to delete all currently selected figures.

        Removes selected shapes from:
        1. The Tkinter Canvas (visually)
        2. The internal data model (self.figures)
        3. The style backup cache (self.changed_figures)

        Can be safely bound to keyboard events (like <Delete>).
        """
        if not self.selected_figures:
            return

        # 1. Collect all shape IDs of the selected figures and remove them from canvas
        selected_ids = set()

        for shape_type, index in self.selected_figures:
            try:
                shape = self.figures[shape_type][index]
                if isinstance(shape, dict):
                    shape_id = shape.get('shape_id')
                else:
                    shape_id = shape[0]

                if shape_id is not None:
                    selected_ids.add(shape_id)
                    # Remove the shape visually from Tkinter Canvas
                    self.canvas.delete(f"id_{shape_id}")
                    # Remove from style restoration cache
                    self.changed_figures.pop(shape_id, None)
            except IndexError:
                continue

        # 2. Rebuild self.figures by filtering out deleted IDs (prevents index-shifting bugs)
        for s_type in list(self.figures.keys()):
            updated_list = []
            for shape in self.figures[s_type]:
                s_id = shape.get('shape_id') if isinstance(
                    shape, dict) else shape[0]
                if s_id not in selected_ids:
                    updated_list.append(shape)
            self.figures[s_type] = updated_list

        # 3. Reset selection states
        self.selected_figures = []
        self.update_tool_options_state()
        self.is_selected = False
        self.actions_panel_controller.on_selection_change(
            self.is_selected)
        self.current = None

    def raise_selected_figures(self) -> None:
        """
        Public method bound to the "layer_up" action button.

        Moves every currently selected figure one level up in the canvas
        stacking order (i.e. swaps each one with whatever figure sits
        immediately above it), relative to other figures only — grid dots,
        panels and the logo are untouched since they don't carry an
        "id_<shape_id>" tag.

        Relative order among the selected figures themselves is preserved,
        so selecting several shapes and raising them moves the whole group
        up together rather than scrambling their order.
        """
        if not self.selected_figures:
            return

        selected_ids = set(self._get_selected_shape_ids())
        if not selected_ids:
            return

        stack = self._get_figure_stack()

        # Walk top -> bottom so a swap never disturbs a pair not yet processed
        for i in range(len(stack) - 2, -1, -1):
            current_id = stack[i]
            above_id = stack[i + 1]

            if current_id in selected_ids and above_id not in selected_ids:
                self.canvas.tag_raise(f"id_{current_id}", f"id_{above_id}")
                stack[i], stack[i + 1] = above_id, current_id

    def lower_selected_figures(self) -> None:
        """
        Public method bound to the "layer_down" action button.

        Moves every currently selected figure one level down in the canvas
        stacking order (i.e. swaps each one with whatever figure sits
        immediately below it), relative to other figures only.

        Relative order among the selected figures themselves is preserved.
        """
        if not self.selected_figures:
            return

        selected_ids = set(self._get_selected_shape_ids())
        if not selected_ids:
            return

        stack = self._get_figure_stack()

        # Walk bottom -> top so a swap never disturbs a pair not yet processed
        for i in range(1, len(stack)):
            current_id = stack[i]
            below_id = stack[i - 1]

            if current_id in selected_ids and below_id not in selected_ids:
                self.canvas.tag_lower(f"id_{current_id}", f"id_{below_id}")
                stack[i], stack[i - 1] = below_id, current_id

    def _sync_tool_options_to_selected_shape(self, current_id: int):
        """
        Detects the styling of the selected shape and updates the Tool Options UI 
        to reflect its current configuration (fill, border, and state).
        """
        if not hasattr(self, 'tool_options_controller') or not self.tool_options_controller:
            return

        # 1. Find the shape type to check if it's a Line or FreeDraw
        shape_type = None
        for s_type, shapes in self.figures.items():
            for shape in shapes:
                if isinstance(shape, dict) and shape.get('shape_id') == current_id:
                    shape_type = s_type
                    break
                elif not isinstance(shape, dict) and shape[0] == current_id:
                    shape_type = s_type
                    break
            if shape_type:
                break

        # --- BLOCK ENTIRE PANEL IF LINE OR FREEDRAW ---
        if shape_type in ('Line', 'FreeDraw'):
            self.tool_options_controller.sync_ui_from_shape(
                "", "", is_disabled=True)
            return

        # 2. Gather style properties from the selection cache or Canvas item
        if current_id in self.changed_figures:
            style = self.changed_figures[current_id]
            fill = style.get("fill", "")
            outline = style.get("outline", "")
            dash = style.get("dash", "")
        else:
            try:
                fill = self.canvas.itemcget(f"id_{current_id}", "fill")
                outline = self.canvas.itemcget(f"id_{current_id}", "outline")
                dash = self.canvas.itemcget(f"id_{current_id}", "dash")
            except Exception:
                return

        # 3. Map values back to ToolOptions configuration IDs
        fill_option = "solid_border"  # Default fallback
        if fill != "" and outline != "":
            fill_option = "solid_border"
        elif fill != "" and outline == "":
            fill_option = "solid_no_border"
        elif fill == "" and outline != "":
            fill_option = "no_solid_border"

        border_option = "solid"  # Default fallback
        if dash and dash != "0" and dash != "":
            border_option = "dotted"
        else:
            border_option = "solid"

        # 4. Trigger UI synchronization (reenables the panel)
        self.tool_options_controller.sync_ui_from_shape(
            fill_option, border_option, is_disabled=False)

    def _on_press(self, event: Event):
        """Step 1: Check if the user clicked on a shape or empty space."""
        self.last_x = event.x
        self.last_y = event.y

        # Reset the movement flag on a new click
        self.has_moved = False

        tolerance = 2
        overlapping_items = self.canvas.find_overlapping(
            event.x - tolerance, event.y - tolerance,
            event.x + tolerance, event.y + tolerance
        )

        clicked_figure = None

        if overlapping_items:
            for item_id in reversed(overlapping_items):
                tags = self.canvas.gettags(item_id)
                shape_id_str = None
                for tag in tags:
                    if tag.startswith("id_"):
                        shape_id_str = tag[3:]
                        break

                if shape_id_str is not None:
                    clicked_figure = self._get_figure_by_model_id(shape_id_str)
                    if clicked_figure:
                        break

        if clicked_figure:
            # If clicked on a new figure outside the current selection, clear the old selection
            if len(self.selected_figures) > 0 and clicked_figure not in self.selected_figures:
                for figure in self.selected_figures:
                    shape = self.figures[figure[0]][figure[1]]

                    if isinstance(shape, dict):
                        # Waiting implement for FreeDraw
                        pass
                    else:
                        shape_id = shape[0]
                        self._select_figure_update_style(
                            shape_id, isSelected=False)

                self.selected_figures = []
                self.update_tool_options_state()
                self.changed_figures.clear()

            shape = self.figures[clicked_figure[0]][clicked_figure[1]]

            if isinstance(shape, dict):
                # FreeDraw change style -> To be implemented
                pass
            else:
                self._select_figure_update_style(shape[0], isSelected=True)

            if clicked_figure not in self.selected_figures:
                self.selected_figures = [clicked_figure]

            self.is_selected = True
            self.update_tool_options_state()
            self.actions_panel_controller.on_selection_change(self.is_selected)

            self.current = None

        else:
            # Clicked on empty space: deselect everything currently selected
            if len(self.selected_figures) > 0:
                for figure in self.selected_figures:
                    shape = self.figures[figure[0]][figure[1]]

                    if isinstance(shape, dict):
                        # Waiting implement for FreeDraw
                        pass
                    else:
                        shape_id = shape[0]
                        self._select_figure_update_style(
                            shape_id, isSelected=False)

            self.selected_figures = []
            self.update_tool_options_state()
            self.changed_figures.clear()
            self.is_selected = False
            self.actions_panel_controller.on_selection_change(self.is_selected)
            self.current = CursorModel()
            self.current.start(event.x, event.y)

    def _on_drag(self, event: Event):
        """Step 2: Either move the selected shapes or draw the selection box."""
        if self.is_selected and self.selected_figures:
            dx = event.x - self.last_x
            dy = event.y - self.last_y

            # Only flag as 'moved' if there is actual displacement
            if dx != 0 or dy != 0:
                self.has_moved = True

                for shape_type, index in self.selected_figures:
                    self._move_figure(shape_type, index, dx, dy)

                self.last_x = event.x
                self.last_y = event.y

        elif self.current is not None:
            self.current.update(event.x, event.y)
            self.view.clear_view_selection()

            self.view.draw(
                self.current.start_x, self.current.start_y,
                self.current.end_x, self.current.end_y,
                outline=self.current.outline_color
            )

    def _on_release(self, event: Event):
        """Step 3: Finish drawing the selection box OR handle auto-deselection."""

        # Case A: Finished drawing an area selection box (dragged in empty space)
        if not self.is_selected and self.current is not None:
            self.view.clear_view_selection()
            start_x, start_y, end_x, end_y = self.current.to_tuple()

            self.selected_figures = self._get_selected_figures(
                start_x, start_y, end_x, end_y
            )

            if self.selected_figures:
                self.is_selected = True

                self.actions_panel_controller.on_selection_change(
                    self.is_selected)

                for figure in self.selected_figures:
                    shape = self.figures[figure[0]][figure[1]]
                    if isinstance(shape, dict):
                        pass
                    else:
                        if shape[0] is not None:
                            self._select_figure_update_style(
                                shape[0], isSelected=True)

        # Case B: Released the mouse while figures were selected
        elif self.is_selected:
            # Auto-deselect ONLY if the figures were dragged/moved.
            # If it was a simple click (has_moved == False), they remain selected.
            if self.has_moved:
                for figure in self.selected_figures:
                    shape = self.figures[figure[0]][figure[1]]
                    if isinstance(shape, dict):
                        pass
                    else:
                        if shape[0] is not None:
                            self._select_figure_update_style(
                                shape[0], isSelected=False)

                self.selected_figures = []
                self.update_tool_options_state()
                self.changed_figures.clear()
                self.is_selected = False
                self.actions_panel_controller.on_selection_change(
                    self.is_selected)

        self.current = None

    def setup(self):
        self.window.bind("<Delete>", self.delete_selected_figures)
        self.window.bind("<BackSpace>", self.delete_selected_figures)

        self.window.bind("<Control-c>", self.copy_shapes)
        self.window.bind("<Control-v>", self.paste_shapes)