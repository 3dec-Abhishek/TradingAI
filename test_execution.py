from agents.execution_agent import ExecutionAgent



agent = ExecutionAgent()



trade = {

    "symbol":"AAPL",

    "type":"CALL",

    "strike":320,

    "expiration":"30D",

    "contracts":2,

    "premium":2.00

}



result = agent.execute(
    trade
)


print(result)