class SectorAllocator:

    def allocate(self, positions):

        sectors={}

        total=sum(

            p["market_value"]

            for p in positions

        )

        for p in positions:

            sector=p.get("sector","Unknown")

            sectors.setdefault(sector,0)

            sectors[sector]+=p["market_value"]

        result=[]

        for s,v in sectors.items():

            result.append({

                "sector":s,

                "allocation":round(

                    100*v/total,

                    2

                )

            })

        return result