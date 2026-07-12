import random



class GeneticOptimizer:



    def optimize(
        self,
        strategies
    ):


        population = strategies



        for generation in range(10):


            population.sort(

                key=lambda x:
                x["score"],

                reverse=True

            )


            survivors = population[:3]


            children=[]


            for s in survivors:


                child=s.copy()


                child["parameter"] += random.uniform(
                    -0.1,
                    0.1
                )


                children.append(
                    child
                )


            population = survivors + children



        return population[0]