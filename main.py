from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

#defining method that will validate if the card is valid or not

def absolute_sum_value(val):
    val = str(val)
    while len(val)!=1:
        val = list(val)
        val = [int(i) for i in val]
        val = sum(val)
        val = str(val)
    return int(val)

def validate_card(cc_number):
    part1 = list(cc_number[-1::-2])
    part2 = list(cc_number[-2::-2])
    part1 = [int(i) for i in part1]
    part2 = [2*int(i) for i in part2]
    part2 = [absolute_sum_value(i) for i in part2]
    final_sum = sum(part1)+sum(part2)
    return final_sum%10
    



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        cc_number = request.form["cc_number"].strip()
        card_number = cc_number
        verdict = validate_card(card_number)
        cc_number = list(cc_number)
        list1 = []
        for i in range(0, len(cc_number), 4):
            list1.append("".join(cc_number[i:i+4]))
            list1.append(" ")
        
        cc_number = "".join(list1)
        cc_number = cc_number.rstrip()



            
        if verdict==0:
            return jsonify({"card_number": cc_number, "validity": "Valid Card"})
        else:
            return jsonify({"card_number": cc_number, "validity": "Invalid Card"})
    
    return render_template("index.html")


if __name__ == '__main__':
    app.run()

