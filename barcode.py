import keyboard

def on_barcode_scanned(e):
    barcode_data = e.name
    process_barcode(barcode_data)

def process_barcode(barcode_data):
    # Implement your logic to handle the scanned barcode data test
    print("Scanned barcode:", barcode_data)

# Register the callback function for key events
keyboard.hook(on_barcode_scanned)

# Keep the script running
keyboard.wait('esc')

print("this is kamran")
