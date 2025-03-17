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

    max_avg_movie = 0
    max_avg_actor = ""
    for line in data:
        fields = parse_csv_line(line.strip())
        actor = fields[0]

        
        try: 
            avg_movie = float(fields[3])
            print(avg_movie)
            if avg_movie > max_avg_movie:
                max_avg_movie = avg_movie
                max_avg_actor = actor
        except ValueError: 
            continue

    result = f"O ator(a) com maior média por filme é {max_avg_actor} com {max_avg_movie}"

print(result)

with open("etapa-3.txt", "w", encoding="utf-8") as output:
    output.write(result)