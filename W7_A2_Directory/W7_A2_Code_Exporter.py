from abc import ABC, abstractmethod
import json

# Abstract Product
class DataExporter(ABC):
    @abstractmethod
    def export(self, data: list):
        pass

# Concrete Product 1
class CSVExporter(DataExporter):
    def export(self, data: list):
        print("\n--- Exporting to CSV ---")
        if not data: return
        headers = ",".join(data[0].keys())
        print(headers)
        for row in data:
            print(",".join(map(str, row.values())))

# Concrete Product 2
class JSONExporter(DataExporter):
    def export(self, data: list):
        print("\n--- Exporting to JSON ---")
        print(json.dumps(data, indent=4))

# Concrete Product 3
class XMLExporter(DataExporter):
    def export(self, data: list):
        print("\n--- Exporting to XML ---")
        xml = "<root>\n"
        for entry in data:
            xml += "  <record>\n"
            for key, value in entry.items():
                xml += f"    <{key}>{value}</{key}>\n"
            xml += "  </record>\n"
        xml += "</root>"
        print(xml)