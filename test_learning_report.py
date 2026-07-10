from reports.learning_report import generate_learning_report



result = {


    "status":"ACTIVE",


    "metrics":{


        "total_trades":10,

        "win_rate":"70%",

        "average_profit":45,

        "average_loss":-20

    },


    "feedback":[


        "BUY signals are performing well",

        "Reduce confidence on low RSI trades"


    ]

}



generate_learning_report(result)