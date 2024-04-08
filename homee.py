import streamlit as st
from PIL import Image
img = Image.open('a12.png')
st.set_page_config(page_title="Mallya National Banks", page_icon=img,initial_sidebar_state="auto",)
st.image(img,use_column_width=False)
def main():
    st.markdown("# **<u><center>Mallya National Banks: Empowering Your Financial Future</center></u>**", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    Welcome to **Mallya National Banks**, where your financial well-being is our top priority. Founded on the principles of trust, innovation, and excellence, we are dedicated to providing unparalleled banking and insurance services tailored to your needs. At Mallya National Banks, we believe in *empowering* individuals and businesses to achieve their financial goals with confidence and integrity. Our motto, "_Empowering Dreams, Securing Futures_," encapsulates our commitment to not only supporting your aspirations but also safeguarding your future.
    """)
    st.markdown("---")
    st.header("Our Policies: Guiding Your Financial Journey")
    st.markdown("""
    ***Customer-Centric Approach***: At Mallya National Banks, our policies are centered around the needs and preferences of our customers. We strive to deliver exceptional service, customized solutions, and seamless experiences at every touchpoint.

    ***Transparency and Accountability***: We uphold the highest standards of transparency and accountability in all our operations. From clear and concise communication to fair and ethical practices, we ensure that our customers can trust us with their financial matters.

    ***Security and Privacy***: Protecting your sensitive information is non-negotiable for us. We implement robust security measures and adhere to strict privacy policies to safeguard your data and give you peace of mind.

    ***Innovation and Adaptability***: As technology evolves, so do we. We embrace innovation and constantly seek ways to enhance our products and services, ensuring that you have access to the latest tools and technologies to manage your finances effectively.
    """)
    st.markdown("---")
    st.markdown("### **<u><center>Principles We Follow: Building Trust Through Integrity</center></u>**", unsafe_allow_html=True)
    st.markdown("""
    * ***Integrity***: We conduct our business with honesty, integrity, and respect for all stakeholders. Our actions are guided by ethical principles, and we always strive to do what is right for our customers and the community.

    * ***Excellence***: We are committed to excellence in everything we do. Whether it's delivering exceptional service, designing innovative products, or fostering a culture of continuous improvement, we set high standards and work tirelessly to exceed them.

    * ***Responsibility***: We recognize our responsibility to society and the environment. Through sustainable practices, community engagement, and responsible lending, we aim to make a positive impact and contribute to the well-being of future generations.

    * ***Collaboration***: We believe in the power of collaboration and partnership. By working together with our customers, employees, and stakeholders, we can achieve greater success and create value for everyone involved.
    """)
    st.markdown("---")
    st.markdown("### **<u><center>Chatbot Assistance</center></u>**", unsafe_allow_html=True)
    st.markdown("""
    Meet our virtual assistant, designed to cater to all your banking and insurance queries:

    **Insurance Expertise**: Whether you're curious about your insurance coverage or need assistance with a claim, our chatbot is your go-to resource for all insurance-related matters.

    **Transaction Support**: Encounter a hiccup with a transaction? Our chatbot swiftly navigates you through resolution steps, ensuring that your banking experience remains hassle-free.

    **Account Insights**: Need to check your balance or review recent transactions? Our chatbot provides instant access to vital account information, empowering you to stay on top of your finances effortlessly.
    """)
    st.markdown("---")
    st.markdown("### **<u><center>Bank Account Page</center></u>**", unsafe_allow_html=True)
    st.markdown("""
    Explore the features of our intuitive bank account page, designed to enhance your banking experience:

    ***Comprehensive Account Details***: Access detailed information about your Mallya National Banks account, including account type, number, and status, all in one convenient location.

    ***Real-time Balance Updates***: Keep tabs on your account balance with our real-time balance overview, ensuring that you're always informed about your financial standing.

    ***Detailed Transaction History***: Dive into your transaction history to track incoming and outgoing payments, allowing you to manage your finances with precision and confidence.

    ***In-depth Information***: From interest rates to account features, our bank account page provides all the information you need to make informed financial decisions tailored to your unique needs.
    """)
    st.markdown("---")
    st.markdown("""
    At ***Mallya National Banks***, we are more than just a financial institution—we are a trusted partner on your journey to financial prosperity. With our customer-centric approach, transparent policies, and commitment to integrity, we strive to build lasting relationships and empower you to reach your financial goals with confidence. Thank you for choosing Mallya National Banks as your preferred banking and insurance provider.
    """)

if __name__ == "__main__":
    main()
