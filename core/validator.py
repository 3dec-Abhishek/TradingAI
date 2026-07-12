class DataValidator:


    @staticmethod
    def ensure_dict(data):

        if isinstance(data, dict):

            return data


        if isinstance(data, list) and len(data):

            if isinstance(data[0], dict):

                return data[0]


        return {}



    @staticmethod
    def ensure_signal(signal):

        if not isinstance(signal, dict):

            return {

                "strategy": "UNKNOWN",

                "signal": "HOLD",

                "confidence": 50

            }


        return signal