class MFreqrel:
    def __init__(self, sdict: dict, event, n: int):
        """
        Initialize the frequency-relativity tracker.

        :param sdict: Dictionary to store event counts.
        :param event: The specific event to track.
        :param n: Total number of events or occurrences.
        """
        if not isinstance(sdict, dict):
            raise ValueError("sdict must be a dictionary.")
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n must be a positive integer.")

        self.sdict = sdict
        self.event = event
        self.n = n

    def update_event_count(self, event, count=1):
        """
        Updates the count of a specific event in the dictionary.

        :param event: Event to update.
        :param count: Number to increment (default is 1).
        """
        if not isinstance(count, int) or count <= 0:
            raise ValueError("Count must be a positive integer.")

        self.sdict[event] = self.sdict.get(event, 0) + count

    def get_event_count(self, event):
        """
        Retrieves the count of a specific event.

        :param event: Event to look up.
        :return: Count of the event.
        """
        return self.sdict.get(event, 0)

    def relative_frequency(self, event):
        """
        Calculates the relative frequency of a specific event.

        :param event: Event to calculate the frequency for.
        :return: Relative frequency (proportion).
        """
        event_count = self.get_event_count(event)
        return event_count / self.n

    def display_frequencies(self):
        """
        Displays all events with their absolute and relative frequencies.
        """
        for event, count in self.sdict.items():
            rel_freq = count / self.n
            print(f"Event: {event}, Count: {count}, Relative Frequency: {rel_freq:.4f}")


