import marimo

__generated_with = "0.13.0"
app = marimo.App()


@app.cell
def _():
    # Initial data definition - exactly as shown in the book
    data = [1, 2, 3]
    return (data,)


@app.cell
def _(data):
    # Cell that depends on data - automatically updates when data changes
    summary = sum(data)
    print("Sum:", summary)
    return


@app.cell
def _():
    # Additional data for demonstration
    data_1 = [10, 20, 30]
    return (data_1,)


if __name__ == "__main__":
    app.run()