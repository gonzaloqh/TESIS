import os

# Procesa cada línea del archivo para extraer las características
def process_line(line):
    parts = line.strip().split(" ||| ")
    features = parts[3]  # Características
    return parse_features(features)

# Convierte la cadena de características en un diccionario de clave-valor
def parse_features(features_str):
    features = {}
    for item in features_str.split():
        if "=" in item:  # Asegurar que el formato sea clave=valor
            key, value = item.split("=", 1)  # Dividir en clave y valor
            # Manejar valores "NA" convirtiéndolos en None, o convertir a float si es posible
            if value == "NA":
                value = None
            else:
                try:
                    value = float(value)
                except ValueError:
                    value = None  # Ignorar si no es un número válido
            # Agregar al diccionario con el prefijo 'features_'
            features[f"features_{key}"] = value
    return features

# Analiza el archivo y calcula los límites de las características
def analyze_features(file_path):
    if not os.path.exists(file_path):
        print(f"El archivo {file_path} no existe.")
        return

    # Diccionario para almacenar los límites de cada característica
    feature_limits = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            features = process_line(line)

            for key, value in features.items():
                if value is None:
                    continue

                if key not in feature_limits:
                    # Inicializar límites para una nueva característica
                    feature_limits[key] = {"min": value, "max": value}
                else:
                    # Actualizar límites existentes
                    feature_limits[key]["min"] = min(feature_limits[key]["min"], value)
                    feature_limits[key]["max"] = max(feature_limits[key]["max"], value)

    # Imprimir resultados
    print("Límites calculados para cada característica:")
    for feature, limits in feature_limits.items():
        print(f"{feature}: Mínimo = {limits['min']}, Máximo = {limits['max']}")

# Ruta al archivo de datos
file_path = "ppdb-2.0-m-all"

# Analizar características del archivo
analyze_features(file_path)

#Límites calculados para cada característica:
#features_PPDB2.0Score: Mínimo = 3.36294, Máximo = 7.18182      
#features_AGigaSim: Mínimo = 0.0, Máximo = 1.0
#features_GoogleNgramSim: Mínimo = 0.0, Máximo = 1.0
#features_Equivalence: Mínimo = 0.0, Máximo = 0.980841
#features_Exclusion: Mínimo = 0.0, Máximo = 0.743102
#features_ForwardEntailment: Mínimo = 0.0, Máximo = 0.998146
#features_Independent: Mínimo = 2e-06, Máximo = 1.0


#features_PPDB1.0Score: Mínimo = 0.00188, Máximo = 27.99295     
#features_Abstract: Mínimo = 0.0, Máximo = 0.0
#features_Adjacent: Mínimo = 0.0, Máximo = 1.0
#features_CharCountDiff: Mínimo = -47.0, Máximo = 50.0
#features_CharLogCR: Mínimo = -2.66259, Máximo = 2.63906
#features_ContainsX: Mínimo = 0.0, Máximo = 1.0
#features_GlueRule: Mínimo = 0.0, Máximo = 0.0
#features_Identity: Mínimo = 0.0, Máximo = 0.0
#features_Lex(e1|e2): Mínimo = -0.11816, Máximo = 63.30685
#features_Lex(e2|e1): Mínimo = 0.0, Máximo = 63.30685
#features_Lexical: Mínimo = 0.0, Máximo = 1.0
#features_LogCount: Mínimo = 0.0, Máximo = 7.02019
#features_Monotonic: Mínimo = 0.0, Máximo = 1.0
#features_OtherRelated: Mínimo = 0.0, Máximo = 0.944571
#features_PhrasePenalty: Mínimo = 1.0, Máximo = 1.0
#features_RarityPenalty: Mínimo = 0.0, Máximo = 0.36788
#features_SourceTerminalsButNoTarget: Mínimo = 0.0, Máximo = 1.0
#features_SourceWords: Mínimo = 0.0, Máximo = 6.0
#features_TargetComplexity: Mínimo = 0.0, Máximo = 1.0
#features_TargetFormality: Mínimo = 0.0, Máximo = 1.0
#features_TargetTerminalsButNoSource: Mínimo = 0.0, Máximo = 1.0
#features_TargetWords: Mínimo = 0.0, Máximo = 6.0
#features_UnalignedSource: Mínimo = 0.0, Máximo = 6.0
#features_UnalignedTarget: Mínimo = 0.0, Máximo = 6.0
#features_WordCountDiff: Mínimo = -5.0, Máximo = 5.0
#features_WordLenDiff: Mínimo = -42.0, Máximo = 22.0
#features_WordLogCR: Mínimo = -1.79176, Máximo = 1.79176
#features_ReverseEntailment: Mínimo = 0.0, Máximo = 0.999058
#features_-logp(LHS|e1): Mínimo = 0.0, Máximo = 13.80577        
#features_-logp(LHS|e2): Mínimo = 0.0, Máximo = 13.67329        
#features_-logp(e1|LHS): Mínimo = 1.50005, Máximo = 16.9991     
#features_-logp(e1|e2): Mínimo = -0.63035, Máximo = 14.0        
#features_-logp(e1|e2,LHS): Mínimo = -0.65959, Máximo = 13.99995
#features_-logp(e2|LHS): Mínimo = 1.50005, Máximo = 16.9991     
#features_-logp(e2|e1): Mínimo = -0.63031, Máximo = 14.0        
#features_-logp(e2|e1,LHS): Mínimo = -0.6596, Máximo = 13.99996 