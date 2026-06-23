from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

# Mock Database: Multiple dummy users data already stored in app memory
USERS_DATABASE = [
    {"name": "Sanjay", "age": 20, "hobby": "coding", "lifestyle": "Morning Person", "cleanliness": "Clean", "budget": 5000},
    {"name": "Karthik", "age": 22, "hobby": "gaming", "lifestyle": "Night Owl", "cleanliness": "Average", "budget": 4500},
    {"name": "Vijay", "age": 21, "hobby": "music", "lifestyle": "Night Owl", "cleanliness": "Messy", "budget": 6000},
    {"name": "Arun", "age": 19, "hobby": "coding", "lifestyle": "Morning Person", "cleanliness": "Clean", "budget": 4800}
]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        current_user = {
            "name": request.form["name"],
            "budget": int(request.form["budget"] or 0),
            "age": request.form["age"],
            "hobby": request.form["hobby"],
            "lifestyle": request.form["lifestyle"],
            "cleanliness": request.form["cleanliness"]
        }

        matches_list = []

        # Comparing current user with all other users in database
        for user in USERS_DATABASE:
            score = 0
            # 1. Lifestyle matching (40 marks)
            if user["lifestyle"] == current_user["lifestyle"]:
                score += 40
            else:
                score += 20
                
            # 2. Cleanliness matching (30 marks)
            if user["cleanliness"] == current_user["cleanliness"]:
                score += 30
            else:
                score += 10
                
            # 3. Hobby matching (30 marks)
            if user["hobby"].lower() == current_user["hobby"].lower():
                score += 30
            else:
                score += 10

            matches_list.append({
                "name": user["name"],
                "age": user["age"],
                "hobby": user["hobby"],
                "lifestyle": user["lifestyle"],
                "cleanliness": user["cleanliness"],
                "score": score
            })

        # Sorting matches based on highest score
        matches_list = sorted(matches_list, key=lambda x: x["score"], reverse=True)

        return render_template("result.html", current_name=current_user["name"], matches=matches_list)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()