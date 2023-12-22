def main():
    degreesCelsius = input("Degrees Celsius: ")
    degreesFahrenheit = input("Degrees Fahrenheit: ")

    if degreesCelsius.isdigit():
        degreesCelsius = int(degreesCelsius)
    else:
        raise ValueError("Please provide a digit.")
    if degreesFahrenheit.isdigit():
        degreesFahrenheit = int(degreesFahrenheit)
    else:
        raise ValueError("Please provide a digit.")  
    
    convertedCelsius = str(convertToCelsius(degreesFahrenheit))
    convertedFarenheight = str(convertToFahrenheit(degreesCelsius))

    print(f"Converted {str(degreesCelsius)} degrees celsius to Fahrenheit is {convertedFarenheight}")
    print(f"Converted {str(degreesFahrenheit)} degrees fahrenheit to to Celsius is {convertedCelsius}")


def convertToFahrenheit(n):
    return n * (9/5) + 32

def convertToCelsius(n):
    return (n - 32) * (5 / 9)

main()