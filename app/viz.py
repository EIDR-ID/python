import asyncio
import tkinter as tk
from tkinter import ttk
from types import NoneType
from typing import Callable, Dict, List, Union

from typing_extensions import TypedDict

from app.manager import SessionManager
from app.services.query import Query
from app.services.response_reader import RegistryRequest


ses = SessionManager.from_default()
empty_exp = {
            "structural_type": None,
            "mode": None,
            "referent_type": None,
            "resource_name": None,
            "alternate_resource_name": None,
            "original_language": None,
            "dubbed_language": None,
            "associated_org": None,
            "release_date": None,
            "country_of_origin": None,
            "status": None,
            "approximate_length": None,
            "alternate_id": None,
            "display_name": None,
            "credits": None,
            "registrant_extra": None,
            "description": None,
}


def snake_to_title(name):
    return name.replace('_', ' ').title()


class DictEditor:
    def __init__(self, data_dict: dict, parent=None, title="Edit Fields"):
        self.data = data_dict
        self.parent = parent
        self.submitted = False

        # Window creation
        if parent:
            self.root = tk.Toplevel(parent)
            self.root.transient(parent)
        else:
            self.root = tk.Tk()

        self.root.title(title)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.create_widgets()

        if not parent:
            self.root.mainloop()

    def create_widgets(self):
        """Create UI elements for the current window"""
        self.entries = {}

        # Clear previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create form elements
        for row, (field_name, value) in enumerate(self.data.items()):
            if isinstance(value, dict):
                # Nested dictionary field
                btn = ttk.Button(
                    self.root,
                    text=f"Edit {snake_to_title(field_name)}",
                    command=lambda fn=field_name: self.edit_nested(fn)
                )
                btn.grid(row=row, columnspan=2, pady=5)

                # Preview label
                # preview = ttk.Label(self.root, text=f"Current value: {value}")
                # preview.grid(row=row + 1, columnspan=2)
                # self.entries[field_name] = {'preview': preview}
            else:
                # Regular field
                text_widget = tk.Text(self.root, height=1, width=30)
                self.entries[field_name] = {
                    'widget': text_widget,
                    'type': type(value) if value is not None else str,
                    'original': value
                }

                ttk.Label(self.root, text=f"{snake_to_title(field_name)}:").grid(
                    row=row, column=0, padx=5, pady=2, sticky="e")

                self.entries[field_name]['widget'].insert("1.0", str(value))
                self.entries[field_name]['widget'].grid(
                    row=row, column=1, padx=5, pady=2, sticky="w")

        # Submit button
        ttk.Button(
            self.root,
            text="Done" if not self.parent else "Save",
            command=self.submit
        ).grid(row=len(self.data) + 2, columnspan=2, pady=10)

    def edit_nested(self, field_name):
        """Open nested dictionary editor"""
        nested_editor = DictEditor(
            self.data[field_name],
            parent=self.root,
            title=f"Editing {snake_to_title(field_name)}"
        )

        # Wait for nested editor to close
        self.root.wait_window(nested_editor.root)

        # Update preview after editing (not implemented)
        # self.entries[field_name]['preview'].config(
        #     text=f"Current value: {self.data[field_name]}"
        # )

    def submit(self):
        """Handle form submission"""
        # Update regular fields
        for field_name, data in self.entries.items():
            if 'widget' in data:
                try:
                    got = data['widget'].get("1.0", "1.end").strip()
                    print(got)
                    if got == "None":
                        self.data[field_name] = None
                    else:
                        self.data[field_name] = data['type'](got)
                except ValueError:
                    self.data[field_name] = data['original']

        self.submitted = True
        self.root.destroy()

    def on_close(self):
        """Handle window closing"""
        if self.parent:
            # Propagate close to parent
            self.root.destroy()
        else:
            # For root window
            self.root.quit()


def display_class_fields(instance, title="Class Fields"):
    root = tk.Tk()
    root.title(title)

    fields = instance if isinstance(instance, Dict) else vars(instance)  # Get instance attributes as a dictionary

    for row, (field_name, value) in enumerate(fields.items()):
        ttk.Label(root, text=f"{snake_to_title(field_name)}:").grid(row=row, column=0, padx=5, pady=2, sticky="e")
        ttk.Label(root, text=str(value)).grid(row=row, column=1, padx=5, pady=2, sticky="w")

    root.mainloop()


def display_instances(instances, title="Instance Browser"):
    root = tk.Tk()
    root.title(title)
    root.geometry("600x400")

    # Create main container
    main_frame = ttk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Create canvas and scrollbar
    canvas = tk.Canvas(main_frame)
    scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    # Configure canvas scrolling
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack elements
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Add mousewheel scrolling
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # Create instance cards
    for idx, instance in enumerate(instances):
        # Get instance identifier (try common attributes)
        identifier = getattr(instance, 'name',
                             getattr(instance, 'id',
                                     f"{(idx + 1) if len(instances) > 1 else ''}"))

        # Instance card frame
        card = ttk.LabelFrame(scrollable_frame,
                              text=f" {identifier} ",
                              relief=tk.RIDGE,
                              borderwidth=2)
        card.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)

        # Get instance fields
        fields = instance if isinstance(instance, dict) else vars(instance)

        # Add fields to card
        for row, (field_name, value) in enumerate(fields.items()):
            ttk.Label(card, text=f"{snake_to_title(field_name)}:").grid(
                row=row, column=0, padx=5, pady=2, sticky="e")
            ttk.Label(card, text=str(value)).grid(
                row=row, column=1, padx=5, pady=2, sticky="w")

    root.mainloop()

def display_editable_dict(data_dict: dict, title: str = "Edit Fields", parent=None):
    # Window management
    is_root = not parent
    root = tk.Toplevel(parent) if parent else tk.Tk()
    root.title(title)

    # Track entries and nested state
    entries = {}
    submitted = False

    # Add keyboard shortcuts
    root.bind("<Return>", lambda e: submit())

    def create_entries():
        nonlocal entries
        entries.clear()

        # Clear existing widgets
        for widget in root.winfo_children():
            widget.destroy()

        # Create form elements
        for row, (field_name, value) in enumerate(data_dict.items()):
            if isinstance(value, dict):
                btn = ttk.Button(
                    root,
                    text=f"Edit {snake_to_title(field_name)}",
                    command=lambda fn=field_name, val=value: edit_nested(fn, val)
                )
                btn.grid(row=row, columnspan=2, pady=5)

                # Display current value
                preview = ttk.Label(root, text=f"{str(value)}")
                preview.grid(row=row + 1, columnspan=2)
                #entries[field_name] = {'preview': preview}
            else:
                # Regular field
                entries[field_name] = {
                    'widget': ttk.Entry(root),
                    'type': type(value),
                    'original': value
                }

                ttk.Label(root, text=f"{snake_to_title(field_name)}:").grid(
                    row=row, column=0, padx=5, pady=2, sticky="e")

                entries[field_name]['widget'].insert(0, str(value))
                entries[field_name]['widget'].grid(
                    row=row, column=1, padx=5, pady=2, sticky="w")

        # Submit button (root window only)
        if is_root:
            ttk.Button(root, text="Done", command=submit).grid(
                row=len(data_dict) + 2, columnspan=2, pady=10)

    def edit_nested(field_name, nested_dict):
        # Create editor window
        editor = tk.Toplevel(root)
        editor.title(f"Editing {snake_to_title(field_name)}")

        # Create nested editor
        display_editable_dict(nested_dict, parent=editor)

        # Wait for nested window to close
        root.wait_window(editor)

        #entries[field_name]['preview'].config(text=f"Current value: {nested_dict}")

    def submit():
        nonlocal submitted
        # Update root dict values
        for field_name, data in entries.items():
            if 'widget' in data:  # Regular field
                try:
                    data_dict[field_name] = data['type'](data['widget'].get())
                except ValueError:
                    data_dict[field_name] = data['original']

        submitted = True
        root.destroy()

    # Initial creation of widgets
    create_entries()

    # Run mainloop only for root window
    if is_root:
        root.mainloop()
        return data_dict if submitted else None
    else:
        # For nested windows, just wait for user interaction
        root.wait_window(root)


def alert_popup(title: str, message: str, label: str = "Alert"):
    # Create the popup window
    popup = tk.Toplevel()
    popup.title(title)

    # Make the window resizable and set a minimum size
    popup.resizable(True, True)
    popup.minsize(300, 150)

    # Add a label with the message
    ttk.Label(popup, text=label, wraplength=400).pack(padx=10, pady=10)

    # Add a selectable text widget
    text_widget = tk.Text(popup, wrap=tk.WORD, height=1, width=50)
    text_widget.insert(tk.END, message)
    text_widget.config(state=tk.DISABLED)  # Make it read-only
    text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Add a close button
    close_button = ttk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)

    # Make the text selectable
    def enable_text_selection(event=None):
        text_widget.config(state=tk.NORMAL)
        text_widget.tag_add(tk.SEL, "1.0", tk.END)
        text_widget.mark_set(tk.INSERT, "1.0")
        text_widget.see(tk.INSERT)
        text_widget.focus_set()

    # Bind double-click to enable text selection
    text_widget.bind("<Double-Button-1>", enable_text_selection)
def render_alert(title: str, message: str, label: str = "Alert"):
    root = tk.Tk()
    root.withdraw()
    alert_popup(title, message, label)
    root.mainloop()

#res = ses.resolve("10.5240/BA24-7B2E-6DBB-D3BC-1721-2")
#display_class_fields(res.base_meta, title=res.base_meta.resource_name)
#display_editable_dict(Query(page_size=0, page_num=0).args, title="Query Fields")

class Vizualizer:
    ses: SessionManager = None
    def __init__(self, ses):
        self.ses = ses

    def display_menu(self):
        root = tk.Tk()
        root.title("EIDR Tools")
        root.geometry("600x400")

        main_frame = ttk.Frame(root)
        #main_frame.pack(fill=tk.BOTH, expand=True)
        ttk.Button(
            root,
            text="Resolve",
            command=self.resolve
        ).grid(row=1, columnspan=2, pady=10)
        ttk.Button(
            root,
            text="Query",
            command=self.query
        ).grid(row=2, columnspan=2, pady=10)

        root.mainloop()




    def query(self):
        #asyncio.run(self.show_expression_builder())
        args = Query(page_size=1, page_num=1).args
        args["expression"] = empty_exp.copy()
        editor = DictEditor(args, title="Query Fields")
        if not editor.submitted:
            raise ValueError("Query cancelled")
        print(args)
        args["expression"] = Query.base_obj_expression(**args["expression"])
        req = RegistryRequest(operations=[Query(**args)])
        res, _ = ses.query(req)
        matches = [r.as_dict() for r in res]
        print(matches)
        display_instances(matches, title="results")
    def resolve(self):
        id = input("Enter an EIDR ID to resolve: ")
        res = ses.resolve(id)
        display_class_fields(res.base_meta, title=res.base_meta.resource_name)

    def show_expression_builder(self):
        data = {
            "structural_type": None,
            "mode": None,
            "referent_type": None,
            "resource_name": None,
            "alternate_resource_name": None,
            "original_language": None,
            "dubbed_language": None,
            "associated_org": None,
            "release_date": None,
            "country_of_origin": None,
            "status": None,
            "approximate_length": None,
            "alternate_id": None,
            "display_name": None,
            "credits": None,
            "registrant_extra": None,
            "description": None,
        }
        asyncio.run(display_editable_dict(data, title="Expression Builder"))
        exp = Query.base_obj_expression(**data)
        render_alert("Expression", exp, "Your expression is:")
        return exp


v = Vizualizer(SessionManager.from_default())
#v.show_expression_builder()

v.query()

#v.resolve()

#v.display_menu()