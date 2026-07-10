from engine.trading_engine import TradingEngine




def main():


    print("\nStarting Trading AI System...\n")


    engine = TradingEngine()



    result = engine.run()



    print("\n")

    print("=" * 60)

    print("TRADING CYCLE COMPLETE")

    print("=" * 60)



    print(

        "Decision:",

        result.get(

            "decision"

        )

    )


    print(

        "Trade:",

        result.get(

            "trade"

        )

    )


    print(

        "Learning:",

        result.get(

            "learning"

        )

    )


    print("=" * 60)





if __name__ == "__main__":


    main()
