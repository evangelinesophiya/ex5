# Ex.05 Design a Website for Server Side Processing
## Date:2/10/2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
~~~
math.html
<!DOCTYPE html>
<html>
<head>
    <title>Lamp Filament Power Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f9f9f9;
            text-align: center;
            padding: 50px;
        }
        form {
            background: #fff;
            padding: 20px;
            border-radius: 10px;
            display: inline-block;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        input {
            margin: 8px;
            padding: 8px;
            border-radius: 5px;
            border: 1px solid #ccc;
            width: 200px;
        }
        button {
            background: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .result, .error {
            margin-top: 20px;
            font-size: 18px;
        }
        .error { color: red; }
    </style>
</head>
<body>
    <h2>Lamp Filament Calculator</h2>
    <p>Formula: <b>P = I² × R</b></p>

    <form method="POST">
        {% csrf_token %}
        <input type="text" name="P" placeholder="Power (P) in W"><br>
        <input type="text" name="I" placeholder="Current (I) in A"><br>
        <input type="text" name="R" placeholder="Resistance (R) in Ω"><br>
        <button type="submit">Calculate</button>
    </form>

    {% if result %}
        <div class="result">{{ result }}</div>
    {% endif %}

    {% if error %}
        <div class="error">{{ error }}</div>
    {% endif %}
</body>
</html>

views.py
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

urls.py
from django.contrib import admin
from django.urls import path
from mathapp.views import index  # Import the view directly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Directly map root URL to the view
]

~~~
## SERVER SIDE PROCESSING:
![alt text](<Screenshot (73).png>)

## HOMEPAGE:
![alt text](<Screenshot 2025-10-03 115248.png>)


## RESULT:
The program for performing server side processing is completed successfully.
