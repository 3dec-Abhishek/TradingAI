def generate_risk_report(result):

    print("\n")
    print("=" * 50)
    print("Risk Analysis")
    print("=" * 50)


    print()


    # Position Size

    position = result.get(
        "position_size",
        {}
    )

    print("Position Size:")
    print(
        f"Value: {position.get('value')}%"
    )
    print(
        f"Limit: {position.get('limit')}%"
    )
    print(
        f"Status: {position.get('status')}"
    )


    print()


    # Options Exposure

    options = result.get(
        "options_exposure",
        {}
    )

    print("Options Exposure:")
    print(
        f"Value: {options.get('value')}%"
    )
    print(
        f"Limit: {options.get('limit')}%"
    )
    print(
        f"Status: {options.get('status')}"
    )


    print()


    # Daily Loss

    loss = result.get(
        "daily_loss",
        {}
    )

    print("Daily Loss:")
    print(
        f"Value: {loss.get('value')}%"
    )
    print(
        f"Limit: {loss.get('limit')}%"
    )
    print(
        f"Status: {loss.get('status')}"
    )


    print()


    # Final Decision

    print(
        "Trade Status:"
    )

    print(
        result.get(
            "trade_status",
            "UNKNOWN"
        )
    )


    print("=" * 50)