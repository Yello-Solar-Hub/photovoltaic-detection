export interface PaymentOptions {
  amount: number;
  currency: string;
}

export function processPayment(options: PaymentOptions) {
  // Placeholder for HyperSwitch API integration
  console.log(`Processing payment of ${options.amount} ${options.currency} via HyperSwitch`);
  return { status: 'success' };
}
