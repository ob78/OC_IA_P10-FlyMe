# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.


class BookingDetails:
    def __init__(
        self,
        origin: str = None,
        destination: str = None,
        start_travel_date: str = None,
        end_travel_date: str = None,
        budget: str = None
    ):
        self.origin = origin
        self.destination = destination
        self.start_travel_date = start_travel_date
        self.end_travel_date = end_travel_date
        self.budget = budget
