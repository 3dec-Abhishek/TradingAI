from learning.metrics import Metrics


class TradeStatistics:

    def __init__(

        self,

        tracker

    ):

        self.tracker = tracker

    ##################################################

    def generate(self):

        trades = self.tracker.get_all_trades()

        statistics = {

            "total_trades":

                len(trades),

            "total_profit":

                Metrics.total_profit(

                    trades

                ),

            "average_profit":

                Metrics.average_profit(

                    trades

                ),

            "average_return":

                Metrics.average_return(

                    trades

                ),

            "win_rate":

                Metrics.win_rate(

                    trades

                ),

            "largest_win":

                Metrics.largest_win(

                    trades

                ),

            "largest_loss":

                Metrics.largest_loss(

                    trades

                ),

            "profit_factor":

                Metrics.profit_factor(

                    trades

                ),

        }

        return statistics