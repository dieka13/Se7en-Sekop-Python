def get_response(prompt, valid_options):
    reply = None
    error_message = "please, input a number " + str(valid_options)

    while True:
        try:
            reply = raw_input(prompt)
            reply = int(reply)

            if reply not in valid_options:
                raise ValueError
            else:
                break

        except ValueError:
            print error_message

    return reply