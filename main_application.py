from customer_agent import CustomerAgent
from product_agent import ProductAgent
from recommendation_engine import RecommendationEngineAgent # type: ignore


def main():
    customer_id = input("Enter Customer ID: ")
    customer_agent = CustomerAgent(customer_id)
    if not customer_agent.profile:
        print("Customer not found!")
        return

    print("Customer Profile:", customer_agent.profile)

    rec_engine = RecommendationEngineAgent()
    recommendations = rec_engine.recommend(customer_agent.profile)

    print("Recommended Products:")
    for product_id in recommendations:
        product_agent = ProductAgent(product_id)
        print(f"- {product_agent.details['Product_ID']} | {product_agent.details['Category']} | {product_agent.details['Brand']} | Price: {product_agent.details['Price']}")


if __name__ == "__main__":
    main()
