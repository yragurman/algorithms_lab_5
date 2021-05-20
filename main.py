
def Knuth_Morris_Pratt_algorithm(the_required_set, basic_text):

    the_required_set_length = len(the_required_set)
    basic_text_length = len(basic_text)

    pi_massive = [0] * len(the_required_set)

    letter_counter = 1
    pairs_counter = 0

    while letter_counter < the_required_set_length:
        if the_required_set[pairs_counter] == the_required_set[letter_counter]:
            pi_massive[letter_counter] = pairs_counter + 1
            letter_counter += 1
            pairs_counter += 1
        else:
            if pairs_counter == 0:
                pi_massive[letter_counter] = 0
                letter_counter += 1
            else:
                pairs_counter = pi_massive[pairs_counter - 1]

    basic_text_counter = 0
    the_required_set_counter = 0

    while basic_text_counter < basic_text_length:
        if basic_text[basic_text_counter] == the_required_set[the_required_set_counter]:
            basic_text_counter += 1
            the_required_set_counter += 1
            if the_required_set_counter == the_required_set_length:
                return "The required set found"
                break
        else:
            if the_required_set_counter > 0:
                the_required_set_counter = pi_massive[the_required_set_counter - 1]
            else:
                basic_text_counter += 1

    if basic_text_counter == basic_text_length and the_required_set_counter != the_required_set_length:
        return "The required set not found"


basic_text = "Peter Piper Picked a Peck of Pickled Peppers"
the_required_set = "Pickled"

print(Knuth_Morris_Pratt_algorithm(the_required_set, basic_text))
