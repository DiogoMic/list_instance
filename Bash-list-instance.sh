#!/bin/bash

# Get a list of all regions
regions=$(aws ec2 describe-regions --query "Regions[].RegionName" --output text)

# Loop through each region and list instances
for region in $regions; do
  echo "Listing instances in region: $region"
  aws ec2 describe-instances --region $region --query 'Reservations[*].Instances[*].[InstanceId,State.Name,InstanceType,Tags[?Key==`Name`].Value|[0]]' --output table
done
