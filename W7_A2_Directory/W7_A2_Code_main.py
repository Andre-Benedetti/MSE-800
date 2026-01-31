from W7_A2_Code_Factory_Class import ExporterFactory

def main():
    # Example Dataset
    dataset = [
        {"id": 1, "name": "Joao", "status": "Active"},
        {"id": 2, "name": "Mario", "status": "Pending"},
        {"id": 3, "name": "Maria", "status": "Pending"}
    ]

    print("--- Data Export System ---")
    format_choice = input("Enter export format (CSV/JSON/XML): ")

    # Using the Factory
    exporter = ExporterFactory.get_exporter(format_choice)

    if exporter:
        exporter.export(dataset)
    else:
        print(f"❌ Error: Format '{format_choice}' is not supported.")

if __name__ == "__main__":
    main()