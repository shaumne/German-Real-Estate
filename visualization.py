import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(df):
    # Set font for proper character display
    plt.rcParams['font.family'] = 'DejaVu Sans'
    
    # Average prices by city
    plt.figure(figsize=(12, 6))
    sns.barplot(x='city', y='price', data=df)
    plt.title('Average Real Estate Prices by City')
    plt.xlabel('City')
    plt.ylabel('Price (€)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('price_analysis.png')
    plt.close()

    # Price per square meter distribution
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='city', y='price_per_sqm', data=df)
    plt.title('Price per Square Meter Distribution by City')
    plt.xlabel('City')
    plt.ylabel('Price per Square Meter (€/m²)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('sqm_price_analysis.png')
    plt.close()

# Get DataFrame from main file and create visualizations
if __name__ == "__main__":
    from german_real_estate_scraper import main
    df = main()
    create_visualizations(df) 