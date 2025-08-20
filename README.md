# Twitter Scraper & Automation 🐦

A powerful and comprehensive Twitter scraper and automation toolkit designed for researchers, marketers, and developers who need to extract and analyze Twitter data at scale.

## ✨ Features

- 🔍 **Advanced Search** - Flexible search with multiple filters and sorting options
- 👥 **Follower Analysis** - Extract followers and following lists with detailed insights
- 📝 **Tweet Scraping** - Scrape tweets and comments at scale with metadata
- 🌟 **KOL Discovery** - Identify and analyze key opinion leaders in your niche
- 📤 **Tweet Automation** - Automate posting tweets with scheduling capabilities
- 💬 **Comment Automation** - Automate commenting and engagement
- 📊 **Data Export** - Export data in multiple formats (JSON, CSV, Excel)
- 🔒 **Rate Limiting** - Built-in rate limiting to respect API limits

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Twitter API access (Bearer token required)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/twitter-scraper.git
cd twitter-scraper
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your API credentials:
```bash
# Set your Twitter API bearer token
export TWITTER_BEARER_TOKEN="your_bearer_token_here"
```

### Basic Usage

#### Advanced Search

```python
import requests

url = "https://api.twitterxapi.com/twitter/advanced_search"

payload = {
    "maxItems": 10,
    "sortBy": "Latest",
    "searchTerms": ["from:elonmusk"]
}

headers = {
    "Authorization": "Bearer your_token_here",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

## 📖 API Reference

### Search Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `maxItems` | integer | Maximum number of tweets to return | 10 |
| `sortBy` | string | Sort order: "Latest", "Popular", "Relevant" | "Latest" |
| `searchTerms` | array | List of search terms and filters | [] |

### Search Filters

- `from:username` - Tweets from specific user
- `to:username` - Tweets mentioning specific user
- `#hashtag` - Tweets with specific hashtag
- `lang:en` - Tweets in specific language
- `since:2023-01-01` - Tweets since date
- `until:2023-12-31` - Tweets until date

## 🔧 Configuration

**Quick Setup for TwitterXAPI:**
1. Sign up at [https://www.twexapi.io/](https://www.twexapi.io/)
2. Get your bearer token from the dashboard
3. Add it to your `.env` file as `TWITTERX_BEARER_TOKEN`
4. Start using the API immediately!

### Alternative: Using Third-party APIs

If you can't get official Twitter API access, you can use third-party services:

#### TwitterXAPI (Current Implementation)

TwitterXAPI is a third-party service that provides easy access to Twitter data without the complexity of official API approval.

**Why Choose TwitterXAPI:**
- ✅ **No Complex Auth** - No OAuth setup required
- ✅ **Instant Access** - Start using immediately with simple API keys
- ✅ **High Performance** - 200+ QPS, far exceeding official API limits
- ✅ **Cost Effective** - Save up to 96% compared to official APIs
- ✅ **99.9% Uptime** - Enterprise-grade reliability

**Getting Started with TwitterXAPI:**

1. **Visit the Website**
   - Go to [TwitterXAPI](https://www.twexapi.io/)
   - Click "Sign In" or "Free Trial" button

2. **Create Your Account**
   - Sign up with your email address
   - Verify your email account
   - Complete the registration process

3. **Get Your API Key**
   - After login, navigate to your dashboard
   - Go to "API Keys" or "Credentials" section
   - Copy your Bearer Token (starts with `twitterx_`)
   - **Important**: Keep this token secure and never share it publicly

4. **Test Your Access**
   ```bash
   curl -X POST "https://api.twitterxapi.com/twitter/advanced_search" \
     -H "Authorization: Bearer twitterx_your_token_here" \
     -H "Content-Type: application/json" \
     -d '{
       "maxItems": 5,
       "sortBy": "Latest",
       "searchTerms": ["from:elonmusk"]
     }'
   ```

5. **Update Your Environment**
   ```env
   # Add to your .env file
   TWITTERX_BEARER_TOKEN=twitterx_your_actual_token_here
   ```

**Pricing Plans:**
- **Free Tier**: Limited API calls for testing
- **Starter**: For small projects and development
- **Pro**: For production applications
- **Enterprise**: Custom solutions with SLA guarantees

**Key Features:**
- Real-time tweet streaming
- Advanced search with filters
- User profile and follower data
- Trending topics and hashtags
- Sentiment analysis capabilities
- Media content extraction

**Support:**
- 24/7 technical support via email: support@twitterxapi.com
- Telegram channel: [@Twitterxapi_Official](https://t.me/Twitterxapi_Official)
- Comprehensive documentation and code examples

#### Other Alternatives
- **RapidAPI Twitter** - Various Twitter API providers
- **Apify Twitter Scraper** - Web scraping approach
- **ScrapingBee** - Managed scraping service

### Security Best Practices

1. **Never commit credentials** to version control
2. **Use environment variables** for all sensitive data
3. **Rotate tokens regularly** for security
4. **Monitor usage** to avoid rate limit violations
5. **Use least privilege** - only request necessary permissions

## 📊 Use Cases

- **Market Research** - Analyze sentiment and trends around brands/products
- **Academic Research** - Collect data for social media studies
- **Competitor Analysis** - Monitor competitor mentions and strategies
- **Influencer Marketing** - Identify and analyze potential brand ambassadors
- **Content Strategy** - Discover trending topics and engagement patterns
- **Crisis Management** - Monitor brand mentions and respond quickly

## ⚠️ Legal and Ethical Considerations

- **Respect Twitter's Terms of Service** - Always comply with Twitter's API terms
- **Rate Limiting** - Don't exceed API rate limits to avoid being blocked
- **Privacy** - Respect user privacy and don't collect personal data unnecessarily
- **Data Usage** - Use scraped data responsibly and in compliance with applicable laws
- **Attribution** - Give proper credit when using or sharing collected data

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Issues and Support

- **Bug Reports** - Please use the [GitHub Issues](https://github.com/yourusername/twitter-scraper/issues) page
- **Feature Requests** - Submit feature requests through GitHub Issues
- **Questions** - For general questions, please check existing issues first

## 🔗 Related Projects

- [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api)
- [Tweepy](https://github.com/tweepy/tweepy) - Twitter API wrapper for Python
- [Selenium Twitter Scraper](https://github.com/bisguzar/twitter-scraper) - Alternative scraping approach

## ⭐ Star History

If you find this project helpful, please consider giving it a star! ⭐

---

**Disclaimer**: This tool is for educational and research purposes. Please ensure compliance with Twitter's Terms of Service and applicable laws in your jurisdiction.
