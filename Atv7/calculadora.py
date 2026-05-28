from flask import Flask, render_template, request
import math

def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]

    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro: número negativo"
            etapas = f"Não existe raiz real de {num1}."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"

        return render_template("calculadora.html", etapas = etapas, resultado = resultado)


    if operacao == "bhaskara":
        num2 = float(request.form["num2"])
        operacao = request.form["operacao"]

        num3 = float(request.form["num3"])
        operacao = request.form["operacao"]

        delta = -((num2**2) - (4 * num1 * num3))
        
        raiz_delta = math.sqrt(delta)
        print(raiz_delta)

        x1 = (-num2 + raiz_delta) / (2 * num1)
        x2 = (-num2 - raiz_delta) / (2 * num1)

        etapas = f"x1 = {x1}, x2 = {x2}"
        resultado = 0

        return render_template("calculadora.html", etapas = etapas, resultado = resultado)


    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )
        num2 = float(num2_valor)

        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"
        
        if operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"

        if operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} * {num2} = {resultado}"

        if operacao == "/":
            resultado = num1 / num2
            etapas = f"{num1} / {num2} = {resultado}"

        if operacao == "^":
            resultado = num1 ** num2
            etapas = f"{num1} ^ {num2} = {resultado}"

        return render_template("calculadora.html", etapas = etapas, resultado = resultado)