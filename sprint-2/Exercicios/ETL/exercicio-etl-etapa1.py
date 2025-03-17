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

    max_movies = 0
    actor_max_movies = ''

    for line in data:
        fields = parse_csv_line(line.strip())
        actor = fields[0]

        try: 
            num_movies = int(fields[2])
            if num_movies > max_movies:
                max_movies = num_movies
                actor_max_movies = actor
        except ValueError: 
            continue
        
    result = f"O ator/atriz com mais filmes é {actor_max_movies}, com {max_movies} filmes."
    
print(result)
    
with open('etapa-1.txt', 'w', encoding='utf-8') as output:
    output.write(result)

