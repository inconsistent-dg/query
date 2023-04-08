import query
import customtkinter as ctk

# Define the calculate_output function
def calculate_output(sequence):
    # Call the function from query.py
    output = query.calculate(sequence)

    # Update the output label
    output_label.configure(text=output)

    # Print the output to the terminal
    print(output)

# gui
## window stuff
ctk.set_appearance_mode("dark")
window = ctk.CTk()
window.title('query')
window.geometry('600x400')
window.configure(fg_color='#000')

## font
unmef = ctk.CTkFont(family="undefined medium", size=20)  # normal size
unmef_small = ctk.CTkFont(family="undefined medium", size=16)  # small size
unmef_large = ctk.CTkFont(family="undefined medium", size=100)  # big label

## widgets
label = ctk.CTkLabel(
    window,
    text="query",
    font=unmef_large,
    text_color='white',
)
label.pack()

# enter a sequence pretty please?
entry_label = ctk.CTkLabel(
    window, 
    font=unmef,
    text="Enter a sequence:",
)
entry_label.pack(pady=5)

# sequence entry
sequence_entry = ctk.CTkEntry(window)
sequence_entry.pack(pady=5)

# calculate button
calculate_button = ctk.CTkButton(window, text="Calculate", font=unmef_small, command=lambda: calculate_output(
    sequence_entry.get()))
calculate_button.pack(pady=5)

# label for output
output_label = ctk.CTkLabel(window, 
    text="The output is: ",
    font=unmef_small,
)
output_label.pack()

# start window loop
window.mainloop()
