import json
import os

from positions.position import Position


class PositionManager:

    def __init__(self):

        self.open_file = "data/open_positions.json"
        self.closed_file = "data/closed_positions.json"

        self.open_positions = []
        self.closed_positions = []

        self.load()

    ##################################################

    def load(self):

        if os.path.exists(self.open_file):

            with open(self.open_file, "r") as f:

                data = json.load(f)

                self.open_positions = [
                    Position.from_dict(p)
                    for p in data
                ]

        if os.path.exists(self.closed_file):

            with open(self.closed_file, "r") as f:

                self.closed_positions = json.load(f)

    ##################################################

    def save(self):

        with open(self.open_file, "w") as f:

            json.dump(

                [p.to_dict() for p in self.open_positions],

                f,

                indent=4

            )

        with open(self.closed_file, "w") as f:

            json.dump(

                self.closed_positions,

                f,

                indent=4

            )

    ##################################################

    def open_position(self, position):

        self.open_positions.append(position)

        self.save()

        return position

    ##################################################

    def close_position(self, position_id):

        for position in self.open_positions:

            if position.id == position_id:

                position.close()

                self.closed_positions.append(

                    position.to_dict()

                )

                self.open_positions.remove(position)

                self.save()

                return position

        return None

    ##################################################

    def update_price(

        self,

        position_id,

        new_price

    ):

        for position in self.open_positions:

            if position.id == position_id:

                position.update_price(

                    new_price

                )

                self.save()

                return position

        return None

    ##################################################

    def get_open_positions(self):

        return self.open_positions

    ##################################################

    def get_closed_positions(self):

        return self.closed_positions