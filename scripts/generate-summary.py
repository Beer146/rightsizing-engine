#!/usr/bin/env python3
"""Generate GitHub Actions summary from analysis results"""

import json
import sys

try:
    with open('analysis-results.json') as f:
        data = json.load(f)
    
    summary = data.get('summary', {})
    savings = summary.get('savings', {})
    total = savings.get('total', {})
    
    print(f"**Total Recommendations:** {summary.get('total_recommendations', 0)}")
    print(f"**Potential Monthly Savings:** ${total.get('monthly_savings', 0):.2f}")
    print(f"**Potential Annual Savings:** ${total.get('annual_savings', 0):.2f}")
    print("")
    
    # Breakdown
    ec2 = savings.get('ec2_rightsizing', {})
    ri = savings.get('reserved_instances', {})
    
    if ec2.get('count', 0) > 0 or ri.get('count', 0) > 0:
        print("### Recommendations Breakdown")
        if ec2.get('count', 0) > 0:
            print(f"- **EC2 Right-Sizing:** {ec2['count']} recommendations (${ec2.get('annual_savings', 0):.2f}/year)")
        if ri.get('count', 0) > 0:
            print(f"- **Reserved Instances:** {ri['count']} recommendations (${ri.get('annual_savings', 0):.2f}/year)")
            
except Exception as e:
    print(f"No actionable recommendations at this time")
    sys.exit(0)