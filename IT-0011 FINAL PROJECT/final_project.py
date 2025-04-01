import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os
from datetime import datetime
import csv

class RecordManager:
    def __init__(self, filename="records.txt"):
        self.filename = filename
        self.data = self._load_data()
    
    def _load_data(self):
        records = []
        
        if not os.path.exists(self.filename):
            return records
        
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    if line.strip():  # Skip empty lines
                        parts = line.strip().split('|')
                        if len(parts) == 5:
                            record = {
                                "first_name": parts[0],
                                "middle_name": parts[1],
                                "last_name": parts[2],
                                "birthday": parts[3],
                                "gender": parts[4]
                            }
                            records.append(record)
            return records
        except Exception:
            return []
    
    def save_data(self):
        try:
            with open(self.filename, 'w') as f:
                for record in self.data:
                    # Format: first|middle|last|birthday|gender
                    line = f"{record['first_name']}|{record['middle_name']}|{record['last_name']}|{record['birthday']}|{record['gender']}\n"
                    f.write(line)
            return True
        except Exception:
            return False
    
    def add_record(self, record):
        self.data.append(record)
        return self.save_data()
    
    def search(self, term):
        term = term.lower()
        results = []
        
        for record in self.data:
            if (term in record["first_name"].lower() or
                term in record["middle_name"].lower() or
                term in record["last_name"].lower()):
                results.append(record)
        
        return results

class PersonalRecordsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Personal Records Manager")
        
        # Set window size to medium-small
        self.master.geometry("600x450")
        
        # Get script directory for saving data in same location
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        data_file = os.path.join(self.script_dir, "records.txt")
        
        # Configure custom styles for better UI
        self.setup_styles()
        
        # Make window responsive
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)
        
        # Initialize the data manager
        self.db = RecordManager(data_file)
        
        # Create the initial screen
        self.show_main_menu()
        
    def setup_styles(self):
        """Setup custom styles for UI components"""
        self.style = ttk.Style()
        
        # Configure colors and fonts
        bg_color = "#f0f0f0"
        accent_color = "#3498db"
        button_bg = "#2980b9" 
        
        # Main styles
        self.style.configure("TFrame", background=bg_color)
        self.style.configure("TLabel", background=bg_color, font=("Helvetica", 10))
        
        # Custom button style
        self.style.configure("Accent.TButton", 
                            font=("Helvetica", 11),
                            background=button_bg,
                            foreground="white")
        
        # Header style
        self.style.configure("Header.TLabel", 
                            font=("Helvetica", 16, "bold"),
                            foreground="#2c3e50",
                            background=bg_color)
        
        # Menu button style
        self.style.configure("Menu.TButton",
                            font=("Helvetica", 12),
                            padding=10)
        
        # Radio button style
        self.style.configure("TRadiobutton", background=bg_color)
        
        # Treeview style for record display
        self.style.configure("Treeview",
                            background="white",
                            foreground="black",
                            rowheight=25,
                            fieldbackground="white")
        self.style.map('Treeview', background=[('selected', accent_color)])
    
    def clear_window(self):
        """Remove all widgets from the window"""
        for widget in self.master.winfo_children():
            widget.destroy()
    
    def show_main_menu(self):
        """Display the main menu screen"""
        self.clear_window()
        
        # Main content frame
        main_frame = ttk.Frame(self.master)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.9, relheight=0.9)
        
        # Title with border bottom
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ttk.Label(header_frame, text="Personal Records Manager", 
                             style="Header.TLabel")
        title_label.pack(pady=10)
        
        # Separator below title
        separator = ttk.Separator(header_frame, orient="horizontal")
        separator.pack(fill=tk.X, pady=(0, 10))
        
        # Menu buttons container with slight animation effect
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(expand=True, fill=tk.BOTH, padx=40)
        
        # Menu buttons
        menu_items = [
            ("Add New Record", self.show_signup_form),
            ("View All Records", self.show_records),
            ("Search Records", self.prompt_search),
            ("Exit", self.master.quit)
        ]
        
        # Helper function for hover effect
        def on_enter(e, btn):
            btn.configure(cursor="hand2")
            
        def on_leave(e, btn):
            btn.configure(cursor="")
        
        # Create menu buttons with consistent spacing
        for idx, (text, command) in enumerate(menu_items):
            btn = ttk.Button(button_frame, text=text, command=command, style="Menu.TButton")
            btn.pack(fill=tk.X, pady=8)
            
            # Add hover effect
            btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b))
            btn.bind("<Leave>", lambda e, b=btn: on_leave(e, b))
            
        # Status bar
        status_frame = ttk.Frame(main_frame)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=(20, 0))
        
        record_count = len(self.db.data)
        status_text = f"{record_count} record{'s' if record_count != 1 else ''} in database"
        
        status = ttk.Label(status_frame, text=status_text, font=("Helvetica", 8))
        status.pack(side=tk.LEFT)
    
    def show_signup_form(self):
        """Show the form to add a new record"""
        self.clear_window()
        
        # Main container
        container = ttk.Frame(self.master)
        container.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.9, relheight=0.9)
        
        # Form header
        header = ttk.Label(container, text="Create New Record", style="Header.TLabel")
        header.pack(anchor=tk.W, pady=(0, 15))
        
        # Separator below title
        separator = ttk.Separator(container, orient="horizontal")
        separator.pack(fill=tk.X, pady=(0, 20))
        
        # Create a canvas with scrollbar for responsiveness
        canvas = tk.Canvas(container, highlightthickness=0, background="#f0f0f0")
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        
        # Form frame will be inside the canvas
        form_frame = ttk.Frame(canvas)
        form_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas.create_window((0, 0), window=form_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Form fields
        fields = [
            ("First Name*", "first_name"),
            ("Middle Name", "middle_name"),
            ("Last Name*", "last_name")
        ]
        
        # Form variables
        form_vars = {}
        
        # Create form fields
        for row, (label_text, field_name) in enumerate(fields):
            field_frame = ttk.Frame(form_frame)
            field_frame.pack(fill=tk.X, pady=8)
            
            label = ttk.Label(field_frame, text=label_text)
            label.pack(anchor=tk.W)
            
            var = tk.StringVar()
            form_vars[field_name] = var
            
            entry = ttk.Entry(field_frame, textvariable=var)
            entry.pack(fill=tk.X, pady=(2, 0))
        
        # Date of birth field with nicer UI
        dob_frame = ttk.Frame(form_frame)
        dob_frame.pack(fill=tk.X, pady=8)
        
        ttk.Label(dob_frame, text="Date of Birth*").pack(anchor=tk.W)
        
        date_select_frame = ttk.Frame(dob_frame)
        date_select_frame.pack(fill=tk.X, pady=(2, 0))
        
        # Month dropdown
        month_var = tk.StringVar()
        form_vars['month'] = month_var
        
        month_names = ["January", "February", "March", "April", "May", "June", 
                      "July", "August", "September", "October", "November", "December"]
        month_combobox = ttk.Combobox(date_select_frame, textvariable=month_var, width=10, 
                                     values=month_names, state="readonly")
        month_combobox.pack(side=tk.LEFT, padx=(0, 5))
        
        # Day dropdown
        day_var = tk.StringVar()
        form_vars['day'] = day_var
        
        day_values = [str(i) for i in range(1, 32)]
        day_combobox = ttk.Combobox(date_select_frame, textvariable=day_var, width=5, 
                                   values=day_values, state="readonly")
        day_combobox.pack(side=tk.LEFT, padx=5)
        
        # Year dropdown
        year_var = tk.StringVar()
        form_vars['year'] = year_var
        
        current_year = datetime.now().year
        year_values = [str(i) for i in range(current_year-100, current_year+1)]
        year_combobox = ttk.Combobox(date_select_frame, textvariable=year_var, width=7, 
                                    values=year_values, state="readonly")
        year_combobox.pack(side=tk.LEFT, padx=5)
        
        # Gender selection
        gender_frame = ttk.Frame(form_frame)
        gender_frame.pack(fill=tk.X, pady=8)
        
        ttk.Label(gender_frame, text="Gender*").pack(anchor=tk.W)
        
        gender_var = tk.StringVar()
        form_vars['gender'] = gender_var
        
        gender_options_frame = ttk.Frame(gender_frame)
        gender_options_frame.pack(fill=tk.X, pady=(2, 0))
        
        gender_options = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]
        
        for i, (text, value) in enumerate(gender_options):
            rb = ttk.Radiobutton(gender_options_frame, text=text, value=value, 
                               variable=gender_var)
            rb.pack(side=tk.LEFT, padx=(0 if i == 0 else 15, 0))
        
        # Required fields note
        note_frame = ttk.Frame(form_frame)
        note_frame.pack(fill=tk.X, pady=(20, 10))
        
        note = ttk.Label(note_frame, text="* Required fields", 
                       font=("Helvetica", 8, "italic"))
        note.pack(side=tk.LEFT)
        
        # Action buttons
        button_frame = ttk.Frame(form_frame)
        button_frame.pack(fill=tk.X, pady=(10, 0))
        
        cancel_btn = ttk.Button(button_frame, text="Cancel", 
                              command=self.show_main_menu)
        cancel_btn.pack(side=tk.LEFT)
        
        save_btn = ttk.Button(button_frame, text="Save Record",
                            command=lambda: self.save_record(form_vars))
        save_btn.pack(side=tk.RIGHT)
    
    def validate_record(self, form_vars):
        """Validate form data before saving"""
        errors = []
        
        # Check required fields
        if not form_vars['first_name'].get().strip():
            errors.append("First name is required")
        if not form_vars['last_name'].get().strip():
            errors.append("Last name is required")
        if not form_vars['gender'].get():
            errors.append("Please select a gender")
            
        # Validate date
        day = form_vars['day'].get()
        month = form_vars['month'].get()
        year = form_vars['year'].get()
        
        if not (day and month and year):
            errors.append("Complete date of birth is required")
        else:
            try:
                # Convert month name to number
                month_num = {
                    "January": "01", "February": "02", "March": "03", "April": "04",
                    "May": "05", "June": "06", "July": "07", "August": "08",
                    "September": "09", "October": "10", "November": "11", "December": "12"
                }.get(month, "01")
                
                # Validate date
                day_str = day.zfill(2)
                date_str = f"{year}-{month_num}-{day_str}"
                datetime.strptime(date_str, "%Y-%m-%d")
            except (ValueError, KeyError):
                errors.append("Invalid date of birth")
        
        return errors
    
    def format_date(self, day, month, year):
        """Format the date as YYYY-MM-DD"""
        month_num = {
            "January": "01", "February": "02", "March": "03", "April": "04",
            "May": "05", "June": "06", "July": "07", "August": "08",
            "September": "09", "October": "10", "November": "11", "December": "12"
        }.get(month, "01")
        
        day_str = day.zfill(2)
        return f"{year}-{month_num}-{day_str}"
    
    def save_record(self, form_vars):
        """Save a new record from the form"""
        # Validate form data
        errors = self.validate_record(form_vars)
        
        if errors:
            error_msg = "\n".join(errors)
            messagebox.showerror("Validation Error", error_msg)
            return
        
        # Format date
        dob = self.format_date(
            form_vars['day'].get(),
            form_vars['month'].get(),
            form_vars['year'].get()
        )
        
        # Create record
        record = {
            "first_name": form_vars['first_name'].get().strip(),
            "middle_name": form_vars['middle_name'].get().strip(),
            "last_name": form_vars['last_name'].get().strip(),
            "birthday": dob,
            "gender": form_vars['gender'].get()
        }
        
        # Save to database
        if self.db.add_record(record):
            messagebox.showinfo("Success", "Record saved successfully!")
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Failed to save record. Please try again.")
    
    def show_records(self, records=None):
        """Display all records or search results"""
        self.clear_window()
        
        # Use all records if none specified
        if records is None:
            records = self.db.data
            title = "All Records"
        else:
            title = "Search Results"
        
        # Main container
        container = ttk.Frame(self.master)
        container.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.9, relheight=0.9)
        
        # Header and search bar
        header_frame = ttk.Frame(container)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(header_frame, text=title, style="Header.TLabel").pack(side=tk.LEFT)
        
        record_count = len(records)
        count_text = f"{record_count} record{'s' if record_count != 1 else ''}"
        ttk.Label(header_frame, text=count_text).pack(side=tk.RIGHT)
        
        # Separator
        separator = ttk.Separator(container, orient="horizontal")
        separator.pack(fill=tk.X, pady=(0, 10))
        
        # Filter bar for all records view
        if title == "All Records" and records:
            filter_frame = ttk.Frame(container)
            filter_frame.pack(fill=tk.X, pady=(0, 10))
            
            ttk.Label(filter_frame, text="Quick Filter:").pack(side=tk.LEFT, padx=(0, 5))
            
            filter_var = tk.StringVar()
            filter_entry = ttk.Entry(filter_frame, textvariable=filter_var)
            filter_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
            
            def apply_filter(*args):
                filter_text = filter_var.get().lower()
                if filter_text:
                    # Clear the treeview
                    for item in tree.get_children():
                        tree.delete(item)
                    
                    # Filter and add matching records
                    for record in records:
                        if (filter_text in record["first_name"].lower() or
                            filter_text in record["last_name"].lower() or
                            filter_text in record["middle_name"].lower()):
                            tree.insert("", "end", values=(
                                record["first_name"],
                                record["middle_name"],
                                record["last_name"],
                                record["birthday"],
                                record["gender"]
                            ))
                else:
                    # Show all records
                    for item in tree.get_children():
                        tree.delete(item)
                    
                    for record in records:
                        tree.insert("", "end", values=(
                            record["first_name"],
                            record["middle_name"],
                            record["last_name"],
                            record["birthday"],
                            record["gender"]
                        ))
            
            filter_var.trace("w", apply_filter)
            
            clear_btn = ttk.Button(filter_frame, text="Clear", width=8,
                                 command=lambda: filter_var.set(""))
            clear_btn.pack(side=tk.RIGHT, padx=(5, 0))
        
        # Create treeview inside a frame (for border effect)
        tree_frame = ttk.Frame(container, style="Card.TFrame")
        tree_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Treeview columns
        columns = ("first_name", "middle_name", "last_name", "birthday", "gender")
        tree = ttk.Treeview(tree_frame, columns=columns, show="headings", selectmode="browse")
        
        # Configure column headings
        tree.heading("first_name", text="First Name")
        tree.heading("middle_name", text="Middle Name")
        tree.heading("last_name", text="Last Name")
        tree.heading("birthday", text="Date of Birth")
        tree.heading("gender", text="Gender")
        
        # Set column widths relative to content
        tree.column("first_name", width=100)
        tree.column("middle_name", width=100)
        tree.column("last_name", width=100)
        tree.column("birthday", width=100)
        tree.column("gender", width=80)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack tree and scrollbar
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Insert records
        if records:
            for record in records:
                tree.insert("", "end", values=(
                    record["first_name"],
                    record["middle_name"],
                    record["last_name"],
                    # Format date for display
                    self.format_date_display(record["birthday"]),
                    record["gender"]
                ))
        else:
            # Show empty state message
            tree.pack_forget()
            scrollbar.pack_forget()
            
            empty_frame = ttk.Frame(tree_frame)
            empty_frame.pack(expand=True, fill=tk.BOTH)
            
            ttk.Label(empty_frame, text="No records found", 
                    font=("Helvetica", 12)).pack(expand=True)
        
        # Buttons
        button_frame = ttk.Frame(container)
        button_frame.pack(fill=tk.X, pady=(10, 0))
        
        back_btn = ttk.Button(button_frame, text="Back to Menu", 
                            command=self.show_main_menu)
        back_btn.pack(side=tk.LEFT)
        
        # Export button if there are records
        if records:
            export_btn = ttk.Button(button_frame, text="Export to CSV", 
                                  command=lambda: self.export_to_csv(records))
            export_btn.pack(side=tk.RIGHT)
    
    def format_date_display(self, date_str):
        """Format date from YYYY-MM-DD to a more readable format"""
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            return date_obj.strftime("%b %d, %Y")
        except ValueError:
            return date_str
    
    def prompt_search(self):
        """Show search dialog with improved UI"""
        search_dlg = tk.Toplevel(self.master)
        search_dlg.title("Search Records")
        search_dlg.geometry("400x150")
        search_dlg.resizable(False, False)
        
        # Make dialog modal
        search_dlg.transient(self.master)
        search_dlg.grab_set()
        
        # Center on parent
        x = self.master.winfo_x() + (self.master.winfo_width() // 2) - (400 // 2)
        y = self.master.winfo_y() + (self.master.winfo_height() // 2) - (150 // 2)
        search_dlg.geometry(f"+{x}+{y}")
        
        # Dialog content
        content_frame = ttk.Frame(search_dlg, padding=20)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(content_frame, text="Enter name to search for:", 
               font=("Helvetica", 12)).pack(anchor=tk.W, pady=(0, 10))
        
        search_var = tk.StringVar()
        search_entry = ttk.Entry(content_frame, textvariable=search_var, width=40)
        search_entry.pack(fill=tk.X, pady=(0, 20))
        search_entry.focus_set()
        
        # Buttons
        btn_frame = ttk.Frame(content_frame)
        btn_frame.pack(fill=tk.X)
        
        ttk.Button(btn_frame, text="Cancel", 
                 command=search_dlg.destroy).pack(side=tk.LEFT)
        
        def do_search():
            term = search_var.get().strip()
            if term:
                search_dlg.destroy()
                results = self.db.search(term)
                self.show_records(results)
            else:
                messagebox.showwarning("Invalid Search", 
                                     "Please enter a search term.")
        
        search_btn = ttk.Button(btn_frame, text="Search",
                              command=do_search)
        search_btn.pack(side=tk.RIGHT)
        
        # Bind enter key to search
        search_dlg.bind("<Return>", lambda e: do_search())
        
        # Wait for dialog to close
        self.master.wait_window(search_dlg)
    
    def export_to_csv(self, records):
        """Export records to CSV file"""
        if not records:
            messagebox.showinfo("Export", "No records to export")
            return
        
        try:
            # Create file in same directory as script
            file_path = os.path.join(self.script_dir, "records_export.csv")
            
            with open(file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                
                # Write header
                writer.writerow(["First Name", "Middle Name", "Last Name", "Date of Birth", "Gender"])
                
                # Write data
                for record in records:
                    writer.writerow([
                        record["first_name"],
                        record["middle_name"],
                        record["last_name"],
                        record["birthday"],
                        record["gender"]
                    ])
            
            messagebox.showinfo("Export Successful", 
                              f"Records exported to {file_path}")
        except Exception as e:
            messagebox.showerror("Export Failed", f"Could not export records: {str(e)}")


if __name__ == "__main__":
    # Set up error handling
    try:
        root = tk.Tk()
        app = PersonalRecordsApp(root)
        
        # Add window icon if available
        try:
            # This would be where you'd add an icon if available
            pass
        except:
            pass
        
        root.mainloop()
    except Exception as e:
        # Handle unexpected errors
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")