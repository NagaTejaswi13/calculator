from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

def index(request):
    return render(request, "index.html")

def basic_calci(request):
    
    # Initialize display and result
    display = ""
    result = None

    # Handle POST request (when buttons are clicked)
    if request.method == "POST":
        # Get the current display value and the clicked button value
        display = request.POST.get("display", "")
        button = request.POST.get("button", "")

        # Check button behavior
        if button == "=":  # Evaluate the expression
            try:
                result = eval(display)  # Evaluate safely
                display = str(result)  # Update display with result
            except Exception as e:
                result = "Error"
                display = ""
        elif button == "c":  # Clear display
            display = ""
        else:  # Append the button value to the display
            display += button

    # Render the page with updated display
    return render(request, "basic_calci.html", {"display": display, "result": result})

def scientific_calci(request):
    return render_to_string("<p>Scientific calculator under construction!</p>")