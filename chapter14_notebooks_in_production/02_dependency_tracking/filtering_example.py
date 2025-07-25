import marimo

__generated_with = "0.13.0"
app = marimo.App()


@app.cell
def _():
    # Cell 1: Define threshold - as shown in book example
    threshold = 30
    return (threshold,)


@app.cell
def _(threshold):
    # Cell 2: Filter data based on threshold - automatically updates when threshold changes
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    filtered_data = [x for x in data if x > threshold]
    print(f"Values greater than {threshold}: {filtered_data}")
    return (data, filtered_data)


@app.cell
def _(filtered_data):
    # Cell 3: Calculate statistics on filtered data
    if filtered_data:
        avg = sum(filtered_data) / len(filtered_data)
        print(f"Average of filtered data: {avg}")
        print(f"Count of filtered values: {len(filtered_data)}")
    else:
        print("No values meet the threshold criteria")
    return


if __name__ == "__main__":
    app.run()