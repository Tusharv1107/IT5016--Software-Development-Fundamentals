# Event Ticket
prices = {
    "VIP":50.0,
    "Regular": 30.0,
    "Student": 20.0
}
return prices.get(category)


def generate_event_ticket(movie, language):
   ticket_price = calculate_ticket_price(language)
   seat_number = generate_random_seat_number()
   
ticket_info = {}
