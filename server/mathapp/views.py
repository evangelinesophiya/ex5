from django.shortcuts import render

def index(request):
    result = None
    error = None

    if request.method == "POST":
        P = request.POST.get("P")
        I = request.POST.get("I")
        R = request.POST.get("R")

        try:
            P = float(P) if P else None
            I = float(I) if I else None
            R = float(R) if R else None

            if I is not None and R is not None and P is None:
                result = f"Power (P) = {I**2 * R:.2f} W"
            elif P is not None and R is not None and I is None:
                I_calc = (P / R) ** 0.5
                result = f"Current (I) = {I_calc:.2f} A"
            elif P is not None and I is not None and R is None:
                R_calc = P / (I**2)
                result = f"Resistance (R) = {R_calc:.2f} Ω"
            else:
                error = "Please provide exactly two values."
        except ValueError:
            error = "Invalid input. Please enter numbers only."

    return render(request, "mathapp/math.html", {"result": result, "error": error})
