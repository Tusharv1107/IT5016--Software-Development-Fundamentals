class Ticket:
    counter = 1
    open_tickets = 0
    closed_tickets = 0
    all_tickets = []

    def __init__(self, staff_id, creator_name, contact_email, description):
        self.ticket_number = Ticket.counter + 2000
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.counter += 1
        Ticket.open_tickets += 1
        Ticket.all_tickets.append(self)

    @staticmethod
    def generate_password(staff_id, creator_name):
        return staff_id[:2] + creator_name[:3]

    def reset_password(self):
        if "Password Change" in self.description:
            new_password = Ticket.generate_password(self.staff_id, self.creator_name)
            self.response = f"New password generated: {new_password}"
            self.status = "Closed"
            Ticket.closed_tickets += 1
            Ticket.open_tickets -= 1

    def respond(self, response):
        self.response = response
        self.status = "Closed"
        Ticket.closed_tickets += 1
        Ticket.open_tickets -= 1

    def reopen(self):
        self.status = "Reopened"
        Ticket.closed_tickets -= 1
        Ticket.open_tickets += 1

    @classmethod
    def ticket_stats(cls):
        return {
            "Tickets Created": cls.counter - 1,
            "Tickets Resolved": cls.closed_tickets,
            "Tickets To Solve": cls.open_tickets
        }

    @classmethod
    def print_all_tickets(cls):
        print("\nPrinting Tickets:")
        for ticket in cls.all_tickets:
            ticket.display()
