class Call(object):
    def __init__(self, idnum, name, number, time, reason):
        self.idnum = idnum
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason

    def display(self):
        print "Call ID: {}".format(self.idnum)
        print "Caller name: {}".format(self.name)
        print "Phone number: {}".format(self.number)
        print "Time of call: {}".format(self.time)
        print "Reason for call: {}".format(self.reason)


class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.q_size = len(self.calls)
        self.total_calls = 0

    def add_call(self, name, number, time, reason):
        self.total_calls += 1
        new_call = Call(self.total_calls, name, number, time, reason)
        self.calls.append(new_call)
        return self

    def info(self):
        for record in self.calls:
            print "Call ID: {}".format(record.idnum)
            print "Caller name: {}".format(record.name)
            print "Phone number: {}".format(record.number)
            print "Time of call: {}".format(record.time)
            print "Reason for call: {}".format(record.reason)


center = CallCenter()
center.add_call("Gary", "444-4444", "4:50", "He's a wuss").add_call("Naomi", "555-5555", "4:55", "Annual checkup")
center.info()
