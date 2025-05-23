export interface SubscriptionOptions {
  planId: string;
  customerId: string;
}

export function createSubscription(options: SubscriptionOptions) {
  // Placeholder for Lago Billing API integration
  console.log(`Creating subscription ${options.planId} for customer ${options.customerId} via Lago Billing`);
  return { status: 'created' };
}
