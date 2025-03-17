def parse_csv_line(line):
    fields = []
    current_field = ""
    inside_quotes = False
    
    for char in line:
        if char == '"':
            inside_quotes = not inside_quotes  
        elif char == ',' and not inside_quotes:
            fields.append(current_field.strip())
            current_field = ""
        else:
            current_field += char
    
    fields.append(current_field.strip())  
    return fields

with open("actors.csv", "r") as file:
    lines = file.readlines()
    data = lines[1:]
    
    frequency = {}

    for line in data:
        fields = parse_csv_line(line.strip())
        movie = fields[4]

        if movie in frequency:
            frequency[movie] += 1
        else:
            frequency[movie] = 1

sorted_movies = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

result = ""
for movie, ocurrences in sorted_movies:
    result += f"O filme {movie} aparece {ocurrences} no dataset.\n"

print(result)

with open("etapa-4.txt", "w", encoding="utf-8") as output:
    output.write(result)
    


