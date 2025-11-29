# 📊 AWS Right-Sizing Recommendation Engine

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![AWS](https://img.shields.io/badge/AWS-boto3-orange.svg)](https://aws.amazon.com/)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

Intelligent AWS cost optimization through deep resource utilization analysis. Analyzes CloudWatch metrics to recommend cheaper instance types, Reserved Instance purchases, and identifies over-provisioned resources.

## 🎯 Features

- 📈 **Deep Metrics Analysis**: Collects 30 days of CloudWatch CPU, memory, network, and disk metrics
- 🔧 **EC2 Right-Sizing**: Recommends smaller instance sizes or cheaper families (Intel → AMD)
- 💳 **Reserved Instance Advisor**: Suggests RI purchases based on consistent usage patterns
- 📊 **ROI Calculations**: Shows exact monthly/annual savings for each recommendation
- 🎨 **Multiple Output Formats**: Console, JSON, CSV, and HTML reports
- 🌍 **Multi-Region Support**: Analyze resources across all AWS regions
- ⚙️ **Configurable Thresholds**: Customize CPU/memory percentiles and minimum savings

## 💡 How It Works

1. **Analyze**: Collects CloudWatch metrics for all running EC2/RDS instances
2. **Calculate**: Determines P95 CPU/memory utilization over 30 days
3. **Recommend**: Suggests optimizations based on actual usage patterns
4. **Save**: Estimates cost savings from each recommendation

### Example Recommendations

- **Downsize**: `m5.xlarge → m5.large` (CPU P95: 15% → Save $70/month)
- **Family Switch**: `m5.large → m5a.large` (Intel → AMD → Save $7/month)
- **Reserved Instance**: Buy 3x `t3.medium` 1-year RI → Save $500/year

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- AWS credentials with CloudWatch read access
- Running EC2/RDS instances with CloudWatch metrics enabled

### Installation
```bash
# Clone the repository
git clone https://github.com/Beer146/rightsizing-engine.git
cd rightsizing-engine

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage
```bash
# Analyze all resources with default settings (30 days)
python src/main.py

# Analyze only EC2 instances
python src/main.py --resources ec2

# Use 60-day analysis period
python src/main.py --lookback-days 60

# Output as JSON
python src/main.py --format json

# Output as CSV for Excel
python src/main.py --format csv
```

## ⚙️ Configuration

Edit `config.yaml` to customize behavior:

### Analysis Settings
```yaml
analysis:
  lookback_days: 30          # Days of metrics to analyze
  cpu_percentile: 95         # Use P95 for peak handling
  min_datapoints: 20         # Minimum data points required
```

### EC2 Recommendations
```yaml
ec2:
  cpu_underutilized_threshold: 20    # % CPU to trigger downsize
  min_savings_threshold: 10          # Minimum $$ to recommend
  allowed_families:                  # Instance families to consider
    - t3
    - m5
    - c5
```

### Reserved Instances
```yaml
reserved_instances:
  min_utilization: 80        # % usage to recommend RI
  term_years: 1              # 1 or 3 year term
  payment_option: partial_upfront
```

## 📊 Example Output
```
💰 RIGHT-SIZING RECOMMENDATION ENGINE - ANALYSIS RESULTS
================================================================================

📊 EXECUTIVE SUMMARY
   Total Recommendations: 12
   Potential Monthly Savings: $245.50
   Potential Annual Savings: $2,946.00

💡 SAVINGS BREAKDOWN
   EC2 Right-Sizing: 8 recommendations → $1,680/year
   Reserved Instances: 4 recommendations → $1,266/year

🔧 EC2 RIGHT-SIZING RECOMMENDATIONS

   DOWNSIZE RECOMMENDATIONS:
   +-------------------+--------+-----------+---------------+---------+-----------------+
   | Instance ID       | Name   | Current   | Recommended   | CPU P95 | Monthly Savings |
   +===================+========+===========+===============+=========+=================+
   | i-0123456789abcdef| WebSrv | m5.xlarge | m5.large      | 18.5%   | $70.08          |
   | i-abcdef123456789 | AppSrv | c5.2xlarge| c5.xlarge     | 22.3%   | $124.10         |
   +-------------------+--------+-----------+---------------+---------+-----------------+

💳 RESERVED INSTANCE RECOMMENDATIONS
   +-----------+---------------+-------+--------+----------------+-----------------+
   | Region    | Instance Type | Count | Term   | Annual Savings | Upfront Payment |
   +===========+===============+=======+========+================+=================+
   | us-east-1 | t3.medium     | 3     | 1 year | $421.20        | $1,054.80       |
   +-----------+---------------+-------+--------+----------------+-----------------+
```

## 🔐 Required IAM Permissions
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "rds:DescribeDBInstances",
        "cloudwatch:GetMetricStatistics"
      ],
      "Resource": "*"
    }
  ]
}
```

## 📁 Project Structure
```
rightsizing-engine/
├── src/
│   ├── analyzers/
│   │   ├── ec2_analyzer.py          # EC2 metrics collector
│   │   └── rds_analyzer.py          # RDS metrics collector
│   ├── recommenders/
│   │   ├── ec2_recommender.py       # Right-sizing logic
│   │   └── reserved_instance_recommender.py
│   ├── cost_optimizer.py            # Savings calculator
│   ├── reporter.py                  # Report generator
│   └── main.py                      # Entry point
├── config.yaml                      # Configuration
├── requirements.txt
└── README.md
```

## 🛣️ Roadmap

- [ ] **Memory-based recommendations** (requires CloudWatch agent)
- [ ] **Auto Scaling Group analysis**
- [ ] **Savings Plans recommendations** (vs Reserved Instances)
- [ ] **EBS volume optimization**
- [ ] **Lambda function right-sizing**
- [ ] **Cost history tracking** over time
- [ ] **Slack/Email notifications**
- [ ] **GitHub Actions scheduling**

## ⚠️ License Notice

This project is licensed under **CC BY-NC-ND 4.0**. This means:
- ✅ You can view and share this code
- ✅ You must give credit if you reference it
- ❌ You cannot use it for commercial purposes
- ❌ You cannot create modified versions

For portfolio review or educational purposes only.

## 🔗 Part of DevOps Portfolio

This is part of my DevOps automation portfolio:
- 🧟 [Zombie Resource Hunter](https://github.com/Beer146/zombie-resource-hunter) - Find unused AWS resources
- 📊 **Right-Sizing Engine** (this project) - Optimize instance sizes
- ✅ Compliance-as-Code Validator (coming soon)
- 📝 Postmortem Generator (coming soon)

---

**Built with ❤️ for cloud cost optimization**