from W7_A2_Code_Exporter import CSVExporter, JSONExporter, XMLExporter

class ExporterFactory:
    @staticmethod
    def get_exporter(format_type: str):
        format_type = format_type.lower().strip()
        
        if format_type == "csv":
            return CSVExporter()
        elif format_type == "json":
            return JSONExporter()
        elif format_type == "xml":
            return XMLExporter()
        else:
            return None