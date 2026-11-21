# BIAN 14.0.0 Service Domain Catalogue (derived)

## Reading guide (applies to every statement below)

- **Source:** BIAN Service Landscape release 14.0.0 specifications held in the GitHub repo `davidamitchell/public`, commit `fe63de7`.
  - OpenAPI 3 specs: `release14.0.0/semantic-apis/oas3 /yamls/<Domain>.yaml` (258 files; note the trailing space in the `oas3 ` directory name).
  - AsyncAPI 3 specs (events): `release14.0.0/semantic-apis/asyncapi-3.x/yamls/<Domain>.yaml`.
  - The ISO 20022 / DDD variants under `release14.0.0/apis-iso20022_ext-ddd/` were not analysed.
- **Everything here is DERIVED** from those files by the script `release14.0.0/semantic-apis/build_knowledge.py`. Nothing comes from bian.org or from model memory.
  Where a grouping or ordering is an inference (not stated in a spec) it is labelled **[derived-rule]**.
- **Traceability:** each fact ends with a citation `File.yaml:<line>` = line number in the original source file
  (OpenAPI unless prefixed `asyncapi:`). The same spec text is in the companion bundles `oas3_yamls_partN.md` under the heading `# FILE: <File>.yaml`
  (bundle line numbers differ; search for the schema / path name quoted next to the citation). All citations were machine-checked: the cited line contains the quoted key.
  A 12-character `sha256` prefix of each source file is given in the catalogue for version pinning.
- **Vocabulary (BIAN):** a *Service Domain* = one spec file. A *Control Record* (CR) is the main managed record of the domain (tag `CR - <Name>`);
  a *Behavior Qualifier* (BQ) is a sub-record/aspect (tag `BQ - <Name>`). Operations have an action code in their summary, e.g. `CoCR` = Control (CR), `ReBQ` = Retrieve (BQ).
- **This document:** a catalogue of every Service Domain (title, purpose, Control Record, Behavior Qualifiers, operation and event counts) plus a **[derived-rule]** grouping into themes.
  The themes are NOT BIAN's official Business Areas / Business Domains; they come from keyword rules applied to each spec's `info.title` (primary) and `info.description` (secondary).
  Each domain shows the matched keyword and where it matched so the grouping can be audited or overridden.

## Theme grouping **[derived-rule]**

Rule: first matching theme (in the order below) for a keyword found in the title; if the title matches nothing, the first match in the description; otherwise `Unclassified`. Keyword patterns are in `build_knowledge.py` (`THEMES`).

### Payments & Settlement (13 domains)
- Bank Drafts (`BankDrafts.yaml`) — matched `payment` in description [BankDrafts.yaml:4]
- Card Clearing (`CardClearing.yaml`) — matched `Clearing` in title [CardClearing.yaml:3]
- Card Financial Settlement (`CardFinancialSettlement.yaml`) — matched `Settle` in title [CardFinancialSettlement.yaml:3]
- Claim Administration (`ClaimAdministration.yaml`) — matched `payment` in description [ClaimAdministration.yaml:4]
- Direct Debit (`DirectDebit.yaml`) — matched `Direct Debit` in title [DirectDebit.yaml:3]
- Direct Debit Mandate (`DirectDebitMandate.yaml`) — matched `Direct Debit` in title [DirectDebitMandate.yaml:3]
- Open Item Management (`OpenItemManagement.yaml`) — matched `payment` in description [OpenItemManagement.yaml:4]
- Payment Order Initiation (`PaymentOrderInitiation.yaml`) — matched `Payment` in title [PaymentOrderInitiation.yaml:3]
- Payment Rail (`PaymentRail.yaml`) — matched `Payment` in title [PaymentRail.yaml:3]
- Standing Order (`StandingOrder.yaml`) — matched `payment` in description [StandingOrder.yaml:4]
- Trade Clearing (`TradeClearing.yaml`) — matched `Clearing` in title [TradeClearing.yaml:3]
- Trade Settlement (`TradeSettlement.yaml`) — matched `Settle` in title [TradeSettlement.yaml:3]
- Transaction Engine (`TransactionEngine.yaml`) — matched `payment` in description [TransactionEngine.yaml:4]

### Cards & Merchant Services (13 domains)
- Card Authorization (`CardAuthorization.yaml`) — matched `Card` in title [CardAuthorization.yaml:3]
- Card Case (`CardCase.yaml`) — matched `Card` in title [CardCase.yaml:3]
- Card Collections (`CardCollections.yaml`) — matched `Card` in title [CardCollections.yaml:3]
- Card Network Participant Facility (`CardNetworkParticipantFacility.yaml`) — matched `Card` in title [CardNetworkParticipantFacility.yaml:3]
- Card Terminal Administration (`CardTerminalAdministration.yaml`) — matched `Card` in title [CardTerminalAdministration.yaml:3]
- Card Terminal Operation (`CardTerminalOperation.yaml`) — matched `Card` in title [CardTerminalOperation.yaml:3]
- Card Transaction Capture (`CardTransactionCapture.yaml`) — matched `Card` in title [CardTransactionCapture.yaml:3]
- Card Transaction Switch (`CardTransactionSwitch.yaml`) — matched `Card` in title [CardTransactionSwitch.yaml:3]
- Card Transaction Tracking (`CardTransactionTracking.yaml`) — matched `Card` in title [CardTransactionTracking.yaml:3]
- Card eCommerce Gateway (`CardeCommerceGateway.yaml`) — matched `Card` in title [CardeCommerceGateway.yaml:3]
- Credit Card (`CreditCard.yaml`) — matched `Card` in title [CreditCard.yaml:3]
- Merchant Acquiring Facility (`MerchantAcquiringFacility.yaml`) — matched `Merchant` in title [MerchantAcquiringFacility.yaml:3]
- Merchant Relations (`MerchantRelations.yaml`) — matched `Merchant` in title [MerchantRelations.yaml:3]

### Lending & Credit (24 domains)
- Bank Guarantee (`BankGuarantee.yaml`) — matched `Guarantee` in title [BankGuarantee.yaml:3]
- Collateral Allocation Management (`CollateralAllocationManagement.yaml`) — matched `Collateral` in title [CollateralAllocationManagement.yaml:3]
- Collateral Asset Administration (`CollateralAssetAdministration.yaml`) — matched `Collateral` in title [CollateralAssetAdministration.yaml:3]
- Consumer Loan (`ConsumerLoan.yaml`) — matched `Loan` in title [ConsumerLoan.yaml:3]
- Corporate Lease (`CorporateLease.yaml`) — matched `loan` in description [CorporateLease.yaml:4]
- Corporate Loan (`CorporateLoan.yaml`) — matched `Loan` in title [CorporateLoan.yaml:3]
- Credit Facility (`CreditFacility.yaml`) — matched `Credit` in title [CreditFacility.yaml:3]
- Credit Management (`CreditManagement.yaml`) — matched `Credit` in title [CreditManagement.yaml:3]
- Credit Risk Models (`CreditRiskModels.yaml`) — matched `Credit` in title [CreditRiskModels.yaml:3]
- Credit Risk Operations (`CreditRiskOperations.yaml`) — matched `Credit` in title [CreditRiskOperations.yaml:3]
- Customer Credit Rating (`CustomerCreditRating.yaml`) — matched `Credit` in title [CustomerCreditRating.yaml:3]
- Disbursement (`Disbursement.yaml`) — matched `loan` in description [Disbursement.yaml:4]
- Factoring (`Factoring.yaml`) — matched `Factoring` in title [Factoring.yaml:3]
- Leasing (`Leasing.yaml`) — matched `Leasing` in title [Leasing.yaml:3]
- Leasing Item Administration (`LeasingItemAdministration.yaml`) — matched `Leasing` in title [LeasingItemAdministration.yaml:3]
- Letter of Credit (`LetterofCredit.yaml`) — matched `Credit` in title [LetterofCredit.yaml:3]
- Loan (`Loan.yaml`) — matched `Loan` in title [Loan.yaml:3]
- Loan Syndication (`LoanSyndication.yaml`) — matched `Loan` in title [LoanSyndication.yaml:3]
- Merchandising Loan (`MerchandisingLoan.yaml`) — matched `Loan` in title [MerchandisingLoan.yaml:3]
- Mortgage Loan (`MortgageLoan.yaml`) — matched `Mortgage` in title [MortgageLoan.yaml:3]
- Notional Pooling (`NotionalPooling.yaml`) — matched `credit` in description [NotionalPooling.yaml:4]
- Stock Lending and Repos (`StockLendingandRepos.yaml`) — matched `Lend` in title [StockLendingandRepos.yaml:3]
- Syndicate Management (`SyndicateManagement.yaml`) — matched `Syndicat` in title [SyndicateManagement.yaml:3]
- Syndicated Loan (`SyndicatedLoan.yaml`) — matched `Syndicat` in title [SyndicatedLoan.yaml:3]

### Securities, Trading & Markets (48 domains)
- Asset And Liability Management (`AssetAndLiabilityManagement.yaml`) — matched `position` in description [AssetAndLiabilityManagement.yaml:4]
- Asset Securitization (`AssetSecuritization.yaml`) — matched `Securit` in title [AssetSecuritization.yaml:3]
- Brokered Product Proxy (`BrokeredProductProxy.yaml`) — matched `Broker` in title [BrokeredProductProxy.yaml:3]
- Commission Agreement (`CommissionAgreement.yaml`) — matched `broker` in description [CommissionAgreement.yaml:4]
- Consumer Investments (`ConsumerInvestments.yaml`) — matched `Investment` in title [ConsumerInvestments.yaml:3]
- Corporate Action (`CorporateAction.yaml`) — matched `custod` in description [CorporateAction.yaml:4]
- Custody Administration (`CustodyAdministration.yaml`) — matched `Custod` in title [CustodyAdministration.yaml:3]
- Customer Portfolio (`CustomerPortfolio.yaml`) — matched `Portfolio` in title [CustomerPortfolio.yaml:3]
- Customer Position (`CustomerPosition.yaml`) — matched `Position` in title [CustomerPosition.yaml:3]
- Dealer Desk (`DealerDesk.yaml`) — matched `trading` in description [DealerDesk.yaml:4]
- ECM And DCM (`ECMAndDCM.yaml`) — matched `bond` in description [ECMAndDCM.yaml:4]
- Financial Instrument Reference Data Management (`FinancialInstrumentReferenceDataManagement.yaml`) — matched `Financial Instrument` in title [FinancialInstrumentReferenceDataManagement.yaml:3]
- Financial Instrument Valuation (`FinancialInstrumentValuation.yaml`) — matched `Financial Instrument` in title [FinancialInstrumentValuation.yaml:3]
- Financial Market Analysis (`FinancialMarketAnalysis.yaml`) — matched `Market` in title [FinancialMarketAnalysis.yaml:3]
- Financial Market Research (`FinancialMarketResearch.yaml`) — matched `Market` in title [FinancialMarketResearch.yaml:3]
- Hedge Fund Administration (`HedgeFundAdministration.yaml`) — matched `Fund` in title [HedgeFundAdministration.yaml:3]
- Intellectual Property Portfolio (`IntellectualPropertyPortfolio.yaml`) — matched `Portfolio` in title [IntellectualPropertyPortfolio.yaml:3]
- Investment Account (`InvestmentAccount.yaml`) — matched `Investment` in title [InvestmentAccount.yaml:3]
- Investment Portfolio Analysis (`InvestmentPortfolioAnalysis.yaml`) — matched `Investment` in title [InvestmentPortfolioAnalysis.yaml:3]
- Investment Portfolio Management (`InvestmentPortfolioManagement.yaml`) — matched `Investment` in title [InvestmentPortfolioManagement.yaml:3]
- Investment Portfolio Planning (`InvestmentPortfolioPlanning.yaml`) — matched `Investment` in title [InvestmentPortfolioPlanning.yaml:3]
- Knowledge Exchange (`KnowledgeExchange.yaml`) — matched `market` in description [KnowledgeExchange.yaml:4]
- Market Analysis (`MarketAnalysis.yaml`) — matched `Market` in title [MarketAnalysis.yaml:3]
- Market Data Switch Operation (`MarketDataSwitchOperation.yaml`) — matched `Market` in title [MarketDataSwitchOperation.yaml:3]
- Market Information Management (`MarketInformationManagement.yaml`) — matched `Market` in title [MarketInformationManagement.yaml:3]
- Market Making (`MarketMaking.yaml`) — matched `Market` in title [MarketMaking.yaml:3]
- Market Order (`MarketOrder.yaml`) — matched `Market` in title [MarketOrder.yaml:3]
- Market Order Execution (`MarketOrderExecution.yaml`) — matched `Market` in title [MarketOrderExecution.yaml:3]
- Market Research (`MarketResearch.yaml`) — matched `Market` in title [MarketResearch.yaml:3]
- Mutual Fund Administration (`MutualFundAdministration.yaml`) — matched `Fund` in title [MutualFundAdministration.yaml:3]
- Order Allocation (`OrderAllocation.yaml`) — matched `market` in description [OrderAllocation.yaml:4]
- Position Keeping (`PositionKeeping.yaml`) — matched `Position` in title [PositionKeeping.yaml:3]
- Position Management (`PositionManagement.yaml`) — matched `Position` in title [PositionManagement.yaml:3]
- Product Portfolio (`ProductPortfolio.yaml`) — matched `Portfolio` in title [ProductPortfolio.yaml:3]
- Program Trading (`ProgramTrading.yaml`) — matched `Trading` in title [ProgramTrading.yaml:3]
- Public Offering (`PublicOffering.yaml`) — matched `securit` in description [PublicOffering.yaml:4]
- Quote Management (`QuoteManagement.yaml`) — matched `trader` in description [QuoteManagement.yaml:4]
- Securities Fails Processing (`SecuritiesFailsProcessing.yaml`) — matched `Securit` in title [SecuritiesFailsProcessing.yaml:3]
- Securities Position Keeping (`SecuritiesPositionKeeping.yaml`) — matched `Securit` in title [SecuritiesPositionKeeping.yaml:3]
- Segment Direction (`SegmentDirection.yaml`) — matched `market` in description [SegmentDirection.yaml:4]
- Sub Custodian Agreement (`SubCustodianAgreement.yaml`) — matched `Custod` in title [SubCustodianAgreement.yaml:3]
- Suitability Checking (`SuitabilityChecking.yaml`) — matched `market` in description [SuitabilityChecking.yaml:4]
- Trade Confirmation Matching (`TradeConfirmationMatching.yaml`) — matched `market` in description [TradeConfirmationMatching.yaml:4]
- Trader Position Operations (`TraderPositionOperations.yaml`) — matched `Trader` in title [TraderPositionOperations.yaml:3]
- Trading Book Oversight (`TradingBookOversight.yaml`) — matched `Trading` in title [TradingBookOversight.yaml:3]
- Underwriting (`Underwriting.yaml`) — matched `Underwrit` in title [Underwriting.yaml:3]
- Unit Trust Administration (`UnitTrustAdministration.yaml`) — matched `investment` in description [UnitTrustAdministration.yaml:4]
- eTrading Workbench (`eTradingWorkbench.yaml`) — matched `Trading` in title [eTradingWorkbench.yaml:3]

### Risk, Compliance & Fraud (16 domains)
- Claim Assessment (`ClaimAssessment.yaml`) — matched `polic` in description [ClaimAssessment.yaml:4]
- Compliance Reporting (`ComplianceReporting.yaml`) — matched `Complian` in title [ComplianceReporting.yaml:3]
- Fraud Diagnosis (`FraudDiagnosis.yaml`) — matched `Fraud` in title [FraudDiagnosis.yaml:3]
- Fraud Evaluation (`FraudEvaluation.yaml`) — matched `Fraud` in title [FraudEvaluation.yaml:3]
- Fraud Model (`FraudModel.yaml`) — matched `Fraud` in title [FraudModel.yaml:3]
- Fraud Resolution (`FraudResolution.yaml`) — matched `Fraud` in title [FraudResolution.yaml:3]
- Funeral Policy (`FuneralPolicy.yaml`) — matched `Polic` in title [FuneralPolicy.yaml:3]
- Guideline Compliance (`GuidelineCompliance.yaml`) — matched `Complian` in title [GuidelineCompliance.yaml:3]
- Internal Audit (`InternalAudit.yaml`) — matched `Audit` in title [InternalAudit.yaml:3]
- Legal Advisory (`LegalAdvisory.yaml`) — matched `Legal` in title [LegalAdvisory.yaml:3]
- Legal Compliance (`LegalCompliance.yaml`) — matched `Legal` in title [LegalCompliance.yaml:3]
- Legal Entity Directory (`LegalEntityDirectory.yaml`) — matched `Legal` in title [LegalEntityDirectory.yaml:3]
- Regulatory And Legal Authority (`RegulatoryAndLegalAuthority.yaml`) — matched `Regulat` in title [RegulatoryAndLegalAuthority.yaml:3]
- Regulatory Compliance (`RegulatoryCompliance.yaml`) — matched `Regulat` in title [RegulatoryCompliance.yaml:3]
- Regulatory Reporting (`RegulatoryReporting.yaml`) — matched `Regulat` in title [RegulatoryReporting.yaml:3]
- Transaction Authorization (`TransactionAuthorization.yaml`) — matched `risk` in description [TransactionAuthorization.yaml:4]

### Deposits & Accounts (16 domains)
- Account Reconciliation (`AccountReconciliation.yaml`) — matched `Account` in title [AccountReconciliation.yaml:3]
- Account Recovery (`AccountRecovery.yaml`) — matched `Account` in title [AccountRecovery.yaml:3]
- Accounts Receivable (`AccountsReceivable.yaml`) — matched `Account` in title [AccountsReceivable.yaml:3]
- Cash Management And Account Services (`CashManagementAndAccountServices.yaml`) — matched `Account` in title [CashManagementAndAccountServices.yaml:3]
- Collections (`Collections.yaml`) — matched `account` in description [Collections.yaml:4]
- Corporate Current Account (`CorporateCurrentAccount.yaml`) — matched `Current Account` in title [CorporateCurrentAccount.yaml:3]
- Current Account (`CurrentAccount.yaml`) — matched `Current Account` in title [CurrentAccount.yaml:3]
- Delinquent Account Handling (`DelinquentAccountHandling.yaml`) — matched `Account` in title [DelinquentAccountHandling.yaml:3]
- Financial Accounting (`FinancialAccounting.yaml`) — matched `Account` in title [FinancialAccounting.yaml:3]
- Incentive Account (`IncentiveAccount.yaml`) — matched `Account` in title [IncentiveAccount.yaml:3]
- Internal Bank Account (`InternalBankAccount.yaml`) — matched `Account` in title [InternalBankAccount.yaml:3]
- Reward Points Account (`RewardPointsAccount.yaml`) — matched `Account` in title [RewardPointsAccount.yaml:3]
- Savings Account (`SavingsAccount.yaml`) — matched `Saving` in title [SavingsAccount.yaml:3]
- Term Deposit (`TermDeposit.yaml`) — matched `Deposit` in title [TermDeposit.yaml:3]
- Term Deposit Framework Agreement (`TermDepositFrameworkAgreement.yaml`) — matched `Deposit` in title [TermDepositFrameworkAgreement.yaml:3]
- Virtual Account (`VirtualAccount.yaml`) — matched `Account` in title [VirtualAccount.yaml:3]

### Customer, Sales & Marketing (64 domains)
- Advertising (`Advertising.yaml`) — matched `Advertis` in title [Advertising.yaml:3]
- Brand Management (`BrandManagement.yaml`) — matched `Brand` in title [BrandManagement.yaml:3]
- Cheque Lock Box (`ChequeLockBox.yaml`) — matched `customer` in description [ChequeLockBox.yaml:4]
- Contact Center Management (`ContactCenterManagement.yaml`) — matched `Contact` in title [ContactCenterManagement.yaml:3]
- Contact Center Operations (`ContactCenterOperations.yaml`) — matched `Contact` in title [ContactCenterOperations.yaml:3]
- Contact Handler (`ContactHandler.yaml`) — matched `Contact` in title [ContactHandler.yaml:3]
- Contact Routing (`ContactRouting.yaml`) — matched `Contact` in title [ContactRouting.yaml:3]
- Correspondent Bank Relationship Management (`CorrespondentBankRelationshipManagement.yaml`) — matched `Relationship` in title [CorrespondentBankRelationshipManagement.yaml:3]
- Counterparty Administration (`CounterpartyAdministration.yaml`) — matched `party` in title [CounterpartyAdministration.yaml:3]
- Customer Access Entitlement (`CustomerAccessEntitlement.yaml`) — matched `Customer` in title [CustomerAccessEntitlement.yaml:3]
- Customer Agreement (`CustomerAgreement.yaml`) — matched `Customer` in title [CustomerAgreement.yaml:3]
- Customer Behavior Insights (`CustomerBehaviorInsights.yaml`) — matched `Customer` in title [CustomerBehaviorInsights.yaml:3]
- Customer Behavior Models (`CustomerBehaviorModels.yaml`) — matched `Customer` in title [CustomerBehaviorModels.yaml:3]
- Customer Billing (`CustomerBilling.yaml`) — matched `Customer` in title [CustomerBilling.yaml:3]
- Customer Campaign Design (`CustomerCampaignDesign.yaml`) — matched `Customer` in title [CustomerCampaignDesign.yaml:3]
- Customer Campaign Execution (`CustomerCampaignExecution.yaml`) — matched `Customer` in title [CustomerCampaignExecution.yaml:3]
- Customer Campaign Management (`CustomerCampaignManagement.yaml`) — matched `Customer` in title [CustomerCampaignManagement.yaml:3]
- Customer Case (`CustomerCase.yaml`) — matched `Customer` in title [CustomerCase.yaml:3]
- Customer Case Management (`CustomerCaseManagement.yaml`) — matched `Customer` in title [CustomerCaseManagement.yaml:3]
- Customer Event History (`CustomerEventHistory.yaml`) — matched `Customer` in title [CustomerEventHistory.yaml:3]
- Customer Financial Insights (`CustomerFinancialInsights.yaml`) — matched `Customer` in title [CustomerFinancialInsights.yaml:3]
- Customer Offer (`CustomerOffer.yaml`) — matched `Customer` in title [CustomerOffer.yaml:3]
- Customer Product And Service Eligibility (`CustomerProductAndServiceEligibility.yaml`) — matched `Customer` in title [CustomerProductAndServiceEligibility.yaml:3]
- Customer Product and Service Directory (`CustomerProductandServiceDirectory.yaml`) — matched `Customer` in title [CustomerProductandServiceDirectory.yaml:3]
- Customer Proposition (`CustomerProposition.yaml`) — matched `Customer` in title [CustomerProposition.yaml:3]
- Customer Relationship Management (`CustomerRelationshipManagement.yaml`) — matched `Customer` in title [CustomerRelationshipManagement.yaml:3]
- Customer Surveys (`CustomerSurveys.yaml`) — matched `Customer` in title [CustomerSurveys.yaml:3]
- Customer Tax Handling (`CustomerTaxHandling.yaml`) — matched `Customer` in title [CustomerTaxHandling.yaml:3]
- Customer Workbench (`CustomerWorkbench.yaml`) — matched `Customer` in title [CustomerWorkbench.yaml:3]
- Fiduciary Agreement (`FiduciaryAgreement.yaml`) — matched `customer` in description [FiduciaryAgreement.yaml:4]
- Interactive Help (`InteractiveHelp.yaml`) — matched `customer` in description [InteractiveHelp.yaml:4]
- Interbank Relationship Management (`InterbankRelationshipManagement.yaml`) — matched `Relationship` in title [InterbankRelationshipManagement.yaml:3]
- Lead and Opportunity Management (`LeadandOpportunityManagement.yaml`) — matched `Lead` in title [LeadandOpportunityManagement.yaml:3]
- Mergers and Acquisitions Advisory (`MergersandAcquisitionsAdvisory.yaml`) — matched `lead` in description [MergersandAcquisitionsAdvisory.yaml:4]
- Operational Gateway (`OperationalGateway.yaml`) — matched `product` in description [OperationalGateway.yaml:4]
- Partner Agreement (`PartnerAgreement.yaml`) — matched `relationship` in description [PartnerAgreement.yaml:4]
- Partner Management (`PartnerManagement.yaml`) — matched `relationship` in description [PartnerManagement.yaml:4]
- Party Asset Directory (`PartyAssetDirectory.yaml`) — matched `Party` in title [PartyAssetDirectory.yaml:3]
- Party Authentication (`PartyAuthentication.yaml`) — matched `Party` in title [PartyAuthentication.yaml:3]
- Party Lifecycle Management (`PartyLifecycleManagement.yaml`) — matched `Party` in title [PartyLifecycleManagement.yaml:3]
- Party Reference Data Directory (`PartyReferenceDataDirectory.yaml`) — matched `Party` in title [PartyReferenceDataDirectory.yaml:3]
- Party Routing Profile (`PartyRoutingProfile.yaml`) — matched `Party` in title [PartyRoutingProfile.yaml:3]
- Private Placement (`PrivatePlacement.yaml`) — matched `customer` in description [PrivatePlacement.yaml:4]
- Processing Order (`ProcessingOrder.yaml`) — matched `customer` in description [ProcessingOrder.yaml:4]
- Product Combination (`ProductCombination.yaml`) — matched `Product` in title [ProductCombination.yaml:3]
- Product Deployment (`ProductDeployment.yaml`) — matched `Product` in title [ProductDeployment.yaml:3]
- Product Design (`ProductDesign.yaml`) — matched `Product` in title [ProductDesign.yaml:3]
- Product Directory (`ProductDirectory.yaml`) — matched `Product` in title [ProductDirectory.yaml:3]
- Product Expert Sales Support (`ProductExpertSalesSupport.yaml`) — matched `Product` in title [ProductExpertSalesSupport.yaml:3]
- Product Inventory Distribution (`ProductInventoryDistribution.yaml`) — matched `Product` in title [ProductInventoryDistribution.yaml:3]
- Product Inventory Item Management (`ProductInventoryItemManagement.yaml`) — matched `Product` in title [ProductInventoryItemManagement.yaml:3]
- Product Matching (`ProductMatching.yaml`) — matched `Product` in title [ProductMatching.yaml:3]
- Product Quality Assurance (`ProductQualityAssurance.yaml`) — matched `Product` in title [ProductQualityAssurance.yaml:3]
- Product Sales Support (`ProductSalesSupport.yaml`) — matched `Product` in title [ProductSalesSupport.yaml:3]
- Product Service Agency (`ProductServiceAgency.yaml`) — matched `Product` in title [ProductServiceAgency.yaml:3]
- Product Training (`ProductTraining.yaml`) — matched `Product` in title [ProductTraining.yaml:3]
- Production Release (`ProductionRelease.yaml`) — matched `Product` in title [ProductionRelease.yaml:3]
- Prospect Campaign Design (`ProspectCampaignDesign.yaml`) — matched `Prospect` in title [ProspectCampaignDesign.yaml:3]
- Prospect Campaign Execution (`ProspectCampaignExecution.yaml`) — matched `Prospect` in title [ProspectCampaignExecution.yaml:3]
- Prospect Campaign Management (`ProspectCampaignManagement.yaml`) — matched `Prospect` in title [ProspectCampaignManagement.yaml:3]
- Reward Points Awards And Redemption (`RewardPointsAwardsAndRedemption.yaml`) — matched `customer` in description [RewardPointsAwardsAndRedemption.yaml:4]
- Rewards Menu (`RewardsMenu.yaml`) — matched `customer` in description [RewardsMenu.yaml:4]
- Sales Product (`SalesProduct.yaml`) — matched `Sales` in title [SalesProduct.yaml:3]
- Sales Product Agreement (`SalesProductAgreement.yaml`) — matched `Sales` in title [SalesProductAgreement.yaml:3]

### Channels & Servicing (19 domains)
- ATM Network Operations (`ATMNetworkOperations.yaml`) — matched `ATM` in title [ATMNetworkOperations.yaml:3]
- Advanced Voice Services Management (`AdvancedVoiceServicesManagement.yaml`) — matched `Voice` in title [AdvancedVoiceServicesManagement.yaml:3]
- Advanced Voice Services Operations (`AdvancedVoiceServicesOperations.yaml`) — matched `Voice` in title [AdvancedVoiceServicesOperations.yaml:3]
- Branch Currency Distribution (`BranchCurrencyDistribution.yaml`) — matched `Branch` in title [BranchCurrencyDistribution.yaml:3]
- Branch Currency Management (`BranchCurrencyManagement.yaml`) — matched `Branch` in title [BranchCurrencyManagement.yaml:3]
- Branch Location Management (`BranchLocationManagement.yaml`) — matched `Branch` in title [BranchLocationManagement.yaml:3]
- Branch Location Operations (`BranchLocationOperations.yaml`) — matched `Branch` in title [BranchLocationOperations.yaml:3]
- Case Root Cause Analysis (`CaseRootCauseAnalysis.yaml`) — matched `Case` in title [CaseRootCauseAnalysis.yaml:3]
- Channel Activity Analysis (`ChannelActivityAnalysis.yaml`) — matched `Channel` in title [ChannelActivityAnalysis.yaml:3]
- Channel Activity History (`ChannelActivityHistory.yaml`) — matched `Channel` in title [ChannelActivityHistory.yaml:3]
- Correspondence (`Correspondence.yaml`) — matched `Correspondence` in title [Correspondence.yaml:3]
- Servicing Activity Analysis (`ServicingActivityAnalysis.yaml`) — matched `Servicing` in title [ServicingActivityAnalysis.yaml:3]
- Servicing Event History (`ServicingEventHistory.yaml`) — matched `Servicing` in title [ServicingEventHistory.yaml:3]
- Servicing Issue (`ServicingIssue.yaml`) — matched `Servicing` in title [ServicingIssue.yaml:3]
- Servicing Mandate (`ServicingMandate.yaml`) — matched `Servicing` in title [ServicingMandate.yaml:3]
- Servicing Order (`ServicingOrder.yaml`) — matched `Servicing` in title [ServicingOrder.yaml:3]
- Session Dialogue (`SessionDialogue.yaml`) — matched `Session` in title [SessionDialogue.yaml:3]
- eBranch Management (`eBranchManagement.yaml`) — matched `Branch` in title [eBranchManagement.yaml:3]
- eBranch Operations (`eBranchOperations.yaml`) — matched `Branch` in title [eBranchOperations.yaml:3]

### Finance, Accounting & Treasury (9 domains)
- Cash Concentration (`CashConcentration.yaml`) — matched `Cash` in title [CashConcentration.yaml:3]
- Central Cash Handling (`CentralCashHandling.yaml`) — matched `Cash` in title [CentralCashHandling.yaml:3]
- Cheque Processing (`ChequeProcessing.yaml`) — matched `financial` in description [ChequeProcessing.yaml:4]
- Corporate Finance (`CorporateFinance.yaml`) — matched `financial` in description [CorporateFinance.yaml:4]
- Corporate Tax Advisory (`CorporateTaxAdvisory.yaml`) — matched `Tax` in title [CorporateTaxAdvisory.yaml:3]
- Corporate Treasury (`CorporateTreasury.yaml`) — matched `Treasury` in title [CorporateTreasury.yaml:3]
- Financial Gateway (`FinancialGateway.yaml`) — matched `Financial` in title [FinancialGateway.yaml:3]
- Financial Statement Assessment (`FinancialStatementAssessment.yaml`) — matched `Financial` in title [FinancialStatementAssessment.yaml:3]
- Promotional Events (`PromotionalEvents.yaml`) — matched `budget` in description [PromotionalEvents.yaml:4]

### Reference & Data Management (13 domains)
- Competitor Analysis (`CompetitorAnalysis.yaml`) — matched `data` in description [CompetitorAnalysis.yaml:4]
- Correspondent Bank Directory (`CorrespondentBankDirectory.yaml`) — matched `Directory` in title [CorrespondentBankDirectory.yaml:3]
- Currency Exchange (`CurrencyExchange.yaml`) — matched `Currency` in title [CurrencyExchange.yaml:3]
- Document Directory (`DocumentDirectory.yaml`) — matched `Directory` in title [DocumentDirectory.yaml:3]
- Incentive Program Directory (`IncentiveProgramDirectory.yaml`) — matched `Directory` in title [IncentiveProgramDirectory.yaml:3]
- Information Provider Operation (`InformationProviderOperation.yaml`) — matched `Information` in title [InformationProviderOperation.yaml:3]
- Issued Certificate Directory (`IssuedCertificateDirectory.yaml`) — matched `Directory` in title [IssuedCertificateDirectory.yaml:3]
- Location Data Management (`LocationDataManagement.yaml`) — matched `Data` in title [LocationDataManagement.yaml:3]
- Management Manual (`ManagementManual.yaml`) — matched `reference` in description [ManagementManual.yaml:4]
- Public Reference Data Management (`PublicReferenceDataManagement.yaml`) — matched `Reference` in title [PublicReferenceDataManagement.yaml:3]
- Service Directory (`ServiceDirectory.yaml`) — matched `Directory` in title [ServiceDirectory.yaml:3]
- Special Pricing Conditions (`SpecialPricingConditions.yaml`) — matched `Pricing` in title [SpecialPricingConditions.yaml:3]
- Trade and Price Reporting (`TradeandPriceReporting.yaml`) — matched `Report` in title [TradeandPriceReporting.yaml:3]

### Corporate Operations & Support (23 domains)
- Archive Services (`ArchiveServices.yaml`) — matched `Archive` in title [ArchiveServices.yaml:3]
- Business Development (`BusinessDevelopment.yaml`) — matched `Business` in title [BusinessDevelopment.yaml:3]
- Business Unit Management (`BusinessUnitManagement.yaml`) — matched `Business` in title [BusinessUnitManagement.yaml:3]
- Commissions (`Commissions.yaml`) — matched `service` in description [Commissions.yaml:4]
- Consumer Advisory Services (`ConsumerAdvisoryServices.yaml`) — matched `Service` in title [ConsumerAdvisoryServices.yaml:3]
- Contractor and Supplier Agreement (`ContractorandSupplierAgreement.yaml`) — matched `Contract` in title [ContractorandSupplierAgreement.yaml:3]
- Corporate Payroll Services (`CorporatePayrollServices.yaml`) — matched `Service` in title [CorporatePayrollServices.yaml:3]
- Corporate Trust Services (`CorporateTrustServices.yaml`) — matched `Service` in title [CorporateTrustServices.yaml:3]
- Document Services (`DocumentServices.yaml`) — matched `Document` in title [DocumentServices.yaml:3]
- Enterprise Architecture (`EnterpriseArchitecture.yaml`) — matched `Enterprise` in title [EnterpriseArchitecture.yaml:3]
- IT Standards And Guidelines (`ITStandardsAndGuidelines.yaml`) — matched `IT` in title [ITStandardsAndGuidelines.yaml:3]
- Issued Device Administration (`IssuedDeviceAdministration.yaml`) — matched `Device` in title [IssuedDeviceAdministration.yaml:3]
- Issued Device Tracking (`IssuedDeviceTracking.yaml`) — matched `Device` in title [IssuedDeviceTracking.yaml:3]
- Operations Log (`OperationsLog.yaml`) — matched `service` in description [OperationsLog.yaml:4]
- Partner Administration (`PartnerAdministration.yaml`) — matched `service` in description [PartnerAdministration.yaml:4]
- Point of Service (`PointofService.yaml`) — matched `Service` in title [PointofService.yaml:3]
- Project Finance (`ProjectFinance.yaml`) — matched `Project` in title [ProjectFinance.yaml:3]
- Rewards Delivery (`RewardsDelivery.yaml`) — matched `service` in description [RewardsDelivery.yaml:4]
- Rewards Inventory (`RewardsInventory.yaml`) — matched `service` in description [RewardsInventory.yaml:4]
- Service Provider Operations (`ServiceProviderOperations.yaml`) — matched `Service` in title [ServiceProviderOperations.yaml:3]
- System Development (`SystemDevelopment.yaml`) — matched `System` in title [SystemDevelopment.yaml:3]
- Systems Administration (`SystemsAdministration.yaml`) — matched `System` in title [SystemsAdministration.yaml:3]
- Trust Services (`TrustServices.yaml`) — matched `Service` in title [TrustServices.yaml:3]

### Unclassified (0 domains)

## Sibling name families **[derived-rule]**

Domains whose CamelCase file name shares a first or last word with at least 2 (first word) or 3 (last word) others. This surfaces pairs such as `*Management` / `*Operations`. Name similarity only; it does not prove a BIAN relationship.

- **ends with Account** (8): Corporate Current Account, Current Account, Incentive Account, Internal Bank Account, Investment Account, Reward Points Account, Savings Account, Virtual Account. Titles cited: [CorporateCurrentAccount.yaml:3], [CurrentAccount.yaml:3], [IncentiveAccount.yaml:3], [InternalBankAccount.yaml:3], [InvestmentAccount.yaml:3], [RewardPointsAccount.yaml:3], [SavingsAccount.yaml:3], [VirtualAccount.yaml:3]
- **ends with Administration** (12): Card Terminal Administration, Claim Administration, Collateral Asset Administration, Counterparty Administration, Custody Administration, Hedge Fund Administration, Issued Device Administration, Leasing Item Administration, Mutual Fund Administration, Partner Administration, Systems Administration, Unit Trust Administration. Titles cited: [CardTerminalAdministration.yaml:3], [ClaimAdministration.yaml:3], [CollateralAssetAdministration.yaml:3], [CounterpartyAdministration.yaml:3], [CustodyAdministration.yaml:3], [HedgeFundAdministration.yaml:3], [IssuedDeviceAdministration.yaml:3], [LeasingItemAdministration.yaml:3], [MutualFundAdministration.yaml:3], [PartnerAdministration.yaml:3], [SystemsAdministration.yaml:3], [UnitTrustAdministration.yaml:3]
- **ends with Advisory** (3): Corporate Tax Advisory, Legal Advisory, Mergers and Acquisitions Advisory. Titles cited: [CorporateTaxAdvisory.yaml:3], [LegalAdvisory.yaml:3], [MergersandAcquisitionsAdvisory.yaml:3]
- **ends with Agreement** (8): Commission Agreement, Contractor and Supplier Agreement, Customer Agreement, Fiduciary Agreement, Partner Agreement, Sales Product Agreement, Sub Custodian Agreement, Term Deposit Framework Agreement. Titles cited: [CommissionAgreement.yaml:3], [ContractorandSupplierAgreement.yaml:3], [CustomerAgreement.yaml:3], [FiduciaryAgreement.yaml:3], [PartnerAgreement.yaml:3], [SalesProductAgreement.yaml:3], [SubCustodianAgreement.yaml:3], [TermDepositFrameworkAgreement.yaml:3]
- **ends with Analysis** (7): Case Root Cause Analysis, Channel Activity Analysis, Competitor Analysis, Financial Market Analysis, Investment Portfolio Analysis, Market Analysis, Servicing Activity Analysis. Titles cited: [CaseRootCauseAnalysis.yaml:3], [ChannelActivityAnalysis.yaml:3], [CompetitorAnalysis.yaml:3], [FinancialMarketAnalysis.yaml:3], [InvestmentPortfolioAnalysis.yaml:3], [MarketAnalysis.yaml:3], [ServicingActivityAnalysis.yaml:3]
- **ends with Compliance** (3): Guideline Compliance, Legal Compliance, Regulatory Compliance. Titles cited: [GuidelineCompliance.yaml:3], [LegalCompliance.yaml:3], [RegulatoryCompliance.yaml:3]
- **ends with Design** (3): Customer Campaign Design, Product Design, Prospect Campaign Design. Titles cited: [CustomerCampaignDesign.yaml:3], [ProductDesign.yaml:3], [ProspectCampaignDesign.yaml:3]
- **ends with Directory** (10): Correspondent Bank Directory, Customer Product and Service Directory, Document Directory, Incentive Program Directory, Issued Certificate Directory, Legal Entity Directory, Party Asset Directory, Party Reference Data Directory, Product Directory, Service Directory. Titles cited: [CorrespondentBankDirectory.yaml:3], [CustomerProductandServiceDirectory.yaml:3], [DocumentDirectory.yaml:3], [IncentiveProgramDirectory.yaml:3], [IssuedCertificateDirectory.yaml:3], [LegalEntityDirectory.yaml:3], [PartyAssetDirectory.yaml:3], [PartyReferenceDataDirectory.yaml:3], [ProductDirectory.yaml:3], [ServiceDirectory.yaml:3]
- **ends with Execution** (3): Customer Campaign Execution, Market Order Execution, Prospect Campaign Execution. Titles cited: [CustomerCampaignExecution.yaml:3], [MarketOrderExecution.yaml:3], [ProspectCampaignExecution.yaml:3]
- **ends with Facility** (3): Card Network Participant Facility, Credit Facility, Merchant Acquiring Facility. Titles cited: [CardNetworkParticipantFacility.yaml:3], [CreditFacility.yaml:3], [MerchantAcquiringFacility.yaml:3]
- **ends with Gateway** (3): Card eCommerce Gateway, Financial Gateway, Operational Gateway. Titles cited: [CardeCommerceGateway.yaml:3], [FinancialGateway.yaml:3], [OperationalGateway.yaml:3]
- **ends with Handling** (3): Central Cash Handling, Customer Tax Handling, Delinquent Account Handling. Titles cited: [CentralCashHandling.yaml:3], [CustomerTaxHandling.yaml:3], [DelinquentAccountHandling.yaml:3]
- **ends with History** (3): Channel Activity History, Customer Event History, Servicing Event History. Titles cited: [ChannelActivityHistory.yaml:3], [CustomerEventHistory.yaml:3], [ServicingEventHistory.yaml:3]
- **ends with Loan** (5): Consumer Loan, Corporate Loan, Merchandising Loan, Mortgage Loan, Syndicated Loan. Titles cited: [ConsumerLoan.yaml:3], [CorporateLoan.yaml:3], [MerchandisingLoan.yaml:3], [MortgageLoan.yaml:3], [SyndicatedLoan.yaml:3]
- **ends with Operation** (3): Card Terminal Operation, Information Provider Operation, Market Data Switch Operation. Titles cited: [CardTerminalOperation.yaml:3], [InformationProviderOperation.yaml:3], [MarketDataSwitchOperation.yaml:3]
- **ends with Operations** (8): ATM Network Operations, Advanced Voice Services Operations, Branch Location Operations, Contact Center Operations, Credit Risk Operations, Service Provider Operations, Trader Position Operations, eBranch Operations. Titles cited: [ATMNetworkOperations.yaml:3], [AdvancedVoiceServicesOperations.yaml:3], [BranchLocationOperations.yaml:3], [ContactCenterOperations.yaml:3], [CreditRiskOperations.yaml:3], [ServiceProviderOperations.yaml:3], [TraderPositionOperations.yaml:3], [eBranchOperations.yaml:3]
- **ends with Order** (4): Market Order, Processing Order, Servicing Order, Standing Order. Titles cited: [MarketOrder.yaml:3], [ProcessingOrder.yaml:3], [ServicingOrder.yaml:3], [StandingOrder.yaml:3]
- **ends with Portfolio** (3): Customer Portfolio, Intellectual Property Portfolio, Product Portfolio. Titles cited: [CustomerPortfolio.yaml:3], [IntellectualPropertyPortfolio.yaml:3], [ProductPortfolio.yaml:3]
- **ends with Reporting** (3): Compliance Reporting, Regulatory Reporting, Trade and Price Reporting. Titles cited: [ComplianceReporting.yaml:3], [RegulatoryReporting.yaml:3], [TradeandPriceReporting.yaml:3]
- **ends with Services** (7): Archive Services, Cash Management And Account Services, Consumer Advisory Services, Corporate Payroll Services, Corporate Trust Services, Document Services, Trust Services. Titles cited: [ArchiveServices.yaml:3], [CashManagementAndAccountServices.yaml:3], [ConsumerAdvisoryServices.yaml:3], [CorporatePayrollServices.yaml:3], [CorporateTrustServices.yaml:3], [DocumentServices.yaml:3], [TrustServices.yaml:3]
- **starts with Account** (2): Account Reconciliation, Account Recovery. Titles cited: [AccountReconciliation.yaml:3], [AccountRecovery.yaml:3]
- **starts with Advanced** (2): Advanced Voice Services Management, Advanced Voice Services Operations. Titles cited: [AdvancedVoiceServicesManagement.yaml:3], [AdvancedVoiceServicesOperations.yaml:3]
- **starts with Asset** (2): Asset And Liability Management, Asset Securitization. Titles cited: [AssetAndLiabilityManagement.yaml:3], [AssetSecuritization.yaml:3]
- **starts with Bank** (2): Bank Drafts, Bank Guarantee. Titles cited: [BankDrafts.yaml:3], [BankGuarantee.yaml:3]
- **starts with Branch** (4): Branch Currency Distribution, Branch Currency Management, Branch Location Management, Branch Location Operations. Titles cited: [BranchCurrencyDistribution.yaml:3], [BranchCurrencyManagement.yaml:3], [BranchLocationManagement.yaml:3], [BranchLocationOperations.yaml:3]
- **starts with Business** (2): Business Development, Business Unit Management. Titles cited: [BusinessDevelopment.yaml:3], [BusinessUnitManagement.yaml:3]
- **starts with Card** (11): Card Authorization, Card Case, Card Clearing, Card Collections, Card Financial Settlement, Card Network Participant Facility, Card Terminal Administration, Card Terminal Operation, Card Transaction Capture, Card Transaction Switch, Card Transaction Tracking. Titles cited: [CardAuthorization.yaml:3], [CardCase.yaml:3], [CardClearing.yaml:3], [CardCollections.yaml:3], [CardFinancialSettlement.yaml:3], [CardNetworkParticipantFacility.yaml:3], [CardTerminalAdministration.yaml:3], [CardTerminalOperation.yaml:3], [CardTransactionCapture.yaml:3], [CardTransactionSwitch.yaml:3], [CardTransactionTracking.yaml:3]
- **starts with Cash** (2): Cash Concentration, Cash Management And Account Services. Titles cited: [CashConcentration.yaml:3], [CashManagementAndAccountServices.yaml:3]
- **starts with Channel** (2): Channel Activity Analysis, Channel Activity History. Titles cited: [ChannelActivityAnalysis.yaml:3], [ChannelActivityHistory.yaml:3]
- **starts with Cheque** (2): Cheque Lock Box, Cheque Processing. Titles cited: [ChequeLockBox.yaml:3], [ChequeProcessing.yaml:3]
- **starts with Claim** (2): Claim Administration, Claim Assessment. Titles cited: [ClaimAdministration.yaml:3], [ClaimAssessment.yaml:3]
- **starts with Collateral** (2): Collateral Allocation Management, Collateral Asset Administration. Titles cited: [CollateralAllocationManagement.yaml:3], [CollateralAssetAdministration.yaml:3]
- **starts with Consumer** (3): Consumer Advisory Services, Consumer Investments, Consumer Loan. Titles cited: [ConsumerAdvisoryServices.yaml:3], [ConsumerInvestments.yaml:3], [ConsumerLoan.yaml:3]
- **starts with Contact** (4): Contact Center Management, Contact Center Operations, Contact Handler, Contact Routing. Titles cited: [ContactCenterManagement.yaml:3], [ContactCenterOperations.yaml:3], [ContactHandler.yaml:3], [ContactRouting.yaml:3]
- **starts with Corporate** (9): Corporate Action, Corporate Current Account, Corporate Finance, Corporate Lease, Corporate Loan, Corporate Payroll Services, Corporate Tax Advisory, Corporate Treasury, Corporate Trust Services. Titles cited: [CorporateAction.yaml:3], [CorporateCurrentAccount.yaml:3], [CorporateFinance.yaml:3], [CorporateLease.yaml:3], [CorporateLoan.yaml:3], [CorporatePayrollServices.yaml:3], [CorporateTaxAdvisory.yaml:3], [CorporateTreasury.yaml:3], [CorporateTrustServices.yaml:3]
- **starts with Correspondent** (2): Correspondent Bank Directory, Correspondent Bank Relationship Management. Titles cited: [CorrespondentBankDirectory.yaml:3], [CorrespondentBankRelationshipManagement.yaml:3]
- **starts with Credit** (5): Credit Card, Credit Facility, Credit Management, Credit Risk Models, Credit Risk Operations. Titles cited: [CreditCard.yaml:3], [CreditFacility.yaml:3], [CreditManagement.yaml:3], [CreditRiskModels.yaml:3], [CreditRiskOperations.yaml:3]
- **starts with Customer** (23): Customer Access Entitlement, Customer Agreement, Customer Behavior Insights, Customer Behavior Models, Customer Billing, Customer Campaign Design, Customer Campaign Execution, Customer Campaign Management, Customer Case, Customer Case Management, Customer Credit Rating, Customer Event History, Customer Financial Insights, Customer Offer, Customer Portfolio, Customer Position, Customer Product And Service Eligibility, Customer Product and Service Directory, Customer Proposition, Customer Relationship Management, Customer Surveys, Customer Tax Handling, Customer Workbench. Titles cited: [CustomerAccessEntitlement.yaml:3], [CustomerAgreement.yaml:3], [CustomerBehaviorInsights.yaml:3], [CustomerBehaviorModels.yaml:3], [CustomerBilling.yaml:3], [CustomerCampaignDesign.yaml:3], [CustomerCampaignExecution.yaml:3], [CustomerCampaignManagement.yaml:3], [CustomerCase.yaml:3], [CustomerCaseManagement.yaml:3], [CustomerCreditRating.yaml:3], [CustomerEventHistory.yaml:3], [CustomerFinancialInsights.yaml:3], [CustomerOffer.yaml:3], [CustomerPortfolio.yaml:3], [CustomerPosition.yaml:3], [CustomerProductAndServiceEligibility.yaml:3], [CustomerProductandServiceDirectory.yaml:3], [CustomerProposition.yaml:3], [CustomerRelationshipManagement.yaml:3], [CustomerSurveys.yaml:3], [CustomerTaxHandling.yaml:3], [CustomerWorkbench.yaml:3]
- **starts with Direct** (2): Direct Debit, Direct Debit Mandate. Titles cited: [DirectDebit.yaml:3], [DirectDebitMandate.yaml:3]
- **starts with Document** (2): Document Directory, Document Services. Titles cited: [DocumentDirectory.yaml:3], [DocumentServices.yaml:3]
- **starts with Financial** (7): Financial Accounting, Financial Gateway, Financial Instrument Reference Data Management, Financial Instrument Valuation, Financial Market Analysis, Financial Market Research, Financial Statement Assessment. Titles cited: [FinancialAccounting.yaml:3], [FinancialGateway.yaml:3], [FinancialInstrumentReferenceDataManagement.yaml:3], [FinancialInstrumentValuation.yaml:3], [FinancialMarketAnalysis.yaml:3], [FinancialMarketResearch.yaml:3], [FinancialStatementAssessment.yaml:3]
- **starts with Fraud** (4): Fraud Diagnosis, Fraud Evaluation, Fraud Model, Fraud Resolution. Titles cited: [FraudDiagnosis.yaml:3], [FraudEvaluation.yaml:3], [FraudModel.yaml:3], [FraudResolution.yaml:3]
- **starts with Incentive** (2): Incentive Account, Incentive Program Directory. Titles cited: [IncentiveAccount.yaml:3], [IncentiveProgramDirectory.yaml:3]
- **starts with Internal** (2): Internal Audit, Internal Bank Account. Titles cited: [InternalAudit.yaml:3], [InternalBankAccount.yaml:3]
- **starts with Investment** (4): Investment Account, Investment Portfolio Analysis, Investment Portfolio Management, Investment Portfolio Planning. Titles cited: [InvestmentAccount.yaml:3], [InvestmentPortfolioAnalysis.yaml:3], [InvestmentPortfolioManagement.yaml:3], [InvestmentPortfolioPlanning.yaml:3]
- **starts with Issued** (3): Issued Certificate Directory, Issued Device Administration, Issued Device Tracking. Titles cited: [IssuedCertificateDirectory.yaml:3], [IssuedDeviceAdministration.yaml:3], [IssuedDeviceTracking.yaml:3]
- **starts with Legal** (3): Legal Advisory, Legal Compliance, Legal Entity Directory. Titles cited: [LegalAdvisory.yaml:3], [LegalCompliance.yaml:3], [LegalEntityDirectory.yaml:3]
- **starts with Market** (7): Market Analysis, Market Data Switch Operation, Market Information Management, Market Making, Market Order, Market Order Execution, Market Research. Titles cited: [MarketAnalysis.yaml:3], [MarketDataSwitchOperation.yaml:3], [MarketInformationManagement.yaml:3], [MarketMaking.yaml:3], [MarketOrder.yaml:3], [MarketOrderExecution.yaml:3], [MarketResearch.yaml:3]
- **starts with Merchant** (2): Merchant Acquiring Facility, Merchant Relations. Titles cited: [MerchantAcquiringFacility.yaml:3], [MerchantRelations.yaml:3]
- **starts with Partner** (3): Partner Administration, Partner Agreement, Partner Management. Titles cited: [PartnerAdministration.yaml:3], [PartnerAgreement.yaml:3], [PartnerManagement.yaml:3]
- **starts with Party** (5): Party Asset Directory, Party Authentication, Party Lifecycle Management, Party Reference Data Directory, Party Routing Profile. Titles cited: [PartyAssetDirectory.yaml:3], [PartyAuthentication.yaml:3], [PartyLifecycleManagement.yaml:3], [PartyReferenceDataDirectory.yaml:3], [PartyRoutingProfile.yaml:3]
- **starts with Payment** (2): Payment Order Initiation, Payment Rail. Titles cited: [PaymentOrderInitiation.yaml:3], [PaymentRail.yaml:3]
- **starts with Position** (2): Position Keeping, Position Management. Titles cited: [PositionKeeping.yaml:3], [PositionManagement.yaml:3]
- **starts with Product** (13): Product Combination, Product Deployment, Product Design, Product Directory, Product Expert Sales Support, Product Inventory Distribution, Product Inventory Item Management, Product Matching, Product Portfolio, Product Quality Assurance, Product Sales Support, Product Service Agency, Product Training. Titles cited: [ProductCombination.yaml:3], [ProductDeployment.yaml:3], [ProductDesign.yaml:3], [ProductDirectory.yaml:3], [ProductExpertSalesSupport.yaml:3], [ProductInventoryDistribution.yaml:3], [ProductInventoryItemManagement.yaml:3], [ProductMatching.yaml:3], [ProductPortfolio.yaml:3], [ProductQualityAssurance.yaml:3], [ProductSalesSupport.yaml:3], [ProductServiceAgency.yaml:3], [ProductTraining.yaml:3]
- **starts with Prospect** (3): Prospect Campaign Design, Prospect Campaign Execution, Prospect Campaign Management. Titles cited: [ProspectCampaignDesign.yaml:3], [ProspectCampaignExecution.yaml:3], [ProspectCampaignManagement.yaml:3]
- **starts with Public** (2): Public Offering, Public Reference Data Management. Titles cited: [PublicOffering.yaml:3], [PublicReferenceDataManagement.yaml:3]
- **starts with Regulatory** (3): Regulatory And Legal Authority, Regulatory Compliance, Regulatory Reporting. Titles cited: [RegulatoryAndLegalAuthority.yaml:3], [RegulatoryCompliance.yaml:3], [RegulatoryReporting.yaml:3]
- **starts with Reward** (2): Reward Points Account, Reward Points Awards And Redemption. Titles cited: [RewardPointsAccount.yaml:3], [RewardPointsAwardsAndRedemption.yaml:3]
- **starts with Rewards** (3): Rewards Delivery, Rewards Inventory, Rewards Menu. Titles cited: [RewardsDelivery.yaml:3], [RewardsInventory.yaml:3], [RewardsMenu.yaml:3]
- **starts with Sales** (2): Sales Product, Sales Product Agreement. Titles cited: [SalesProduct.yaml:3], [SalesProductAgreement.yaml:3]
- **starts with Securities** (2): Securities Fails Processing, Securities Position Keeping. Titles cited: [SecuritiesFailsProcessing.yaml:3], [SecuritiesPositionKeeping.yaml:3]
- **starts with Service** (2): Service Directory, Service Provider Operations. Titles cited: [ServiceDirectory.yaml:3], [ServiceProviderOperations.yaml:3]
- **starts with Servicing** (5): Servicing Activity Analysis, Servicing Event History, Servicing Issue, Servicing Mandate, Servicing Order. Titles cited: [ServicingActivityAnalysis.yaml:3], [ServicingEventHistory.yaml:3], [ServicingIssue.yaml:3], [ServicingMandate.yaml:3], [ServicingOrder.yaml:3]
- **starts with Term** (2): Term Deposit, Term Deposit Framework Agreement. Titles cited: [TermDeposit.yaml:3], [TermDepositFrameworkAgreement.yaml:3]
- **starts with Trade** (3): Trade Clearing, Trade Confirmation Matching, Trade Settlement. Titles cited: [TradeClearing.yaml:3], [TradeConfirmationMatching.yaml:3], [TradeSettlement.yaml:3]
- **starts with Transaction** (2): Transaction Authorization, Transaction Engine. Titles cited: [TransactionAuthorization.yaml:3], [TransactionEngine.yaml:3]
- **starts with e** (3): eBranch Management, eBranch Operations, eTrading Workbench. Titles cited: [eBranchManagement.yaml:3], [eBranchOperations.yaml:3], [eTradingWorkbench.yaml:3]

## Action codes seen in operation summaries **(observed)**

Code = first word of an operation `summary`; term = last path segment of that operation. Example citation is the first occurrence.

| Code | Term(s) in URL path | Operations | Example |
|---|---|---|---|
| CaBQ | Capture (93) | 93 | BranchCurrencyManagement.yaml:167: CaBQ Capture Inventory Allocation activity or event related informatio |
| CaCR | Capture (22) | 22 | BranchCurrencyManagement.yaml:12: CaCR Capture Branch Cash Allocation activity or event related informat |
| CoBQ | Control (27) | 27 | ATMNetworkOperations.yaml:193: CoBQ Control the processing of Network Operation |
| CoCR | Control (109) | 109 | ATMNetworkOperations.yaml:12: CoCR Control the processing of ATM Network Operating Session |
| CrBQ | Create (27) | 27 | AdvancedVoiceServicesManagement.yaml:271: CrBQ Create a maintenance or upgrade task plan item for the channel |
| CrCR | Create (24) | 24 | AdvancedVoiceServicesManagement.yaml:12: CrCR Create the management plan for the voice channel |
| EcBQ | Exchange (164), Execute (1) | 165 | ATMNetworkOperations.yaml:116: EcBQ Accept, verify, etc. aspects of Cash Distribution processing |
| EcCR | Exchange (96) | 96 | ATMNetworkOperations.yaml:38: EcCR Accept, verify, etc. aspects of ATM Network Operating Session pro |
| EvBQ | Evaluate (26), Initiate (1) | 27 | CustomerAccessEntitlement.yaml:217: EvBQ Establish restrictions for the access profile agreement |
| EvCR | Evaluate (27), Initiate (1) | 28 | CardAuthorization.yaml:38: EvCR Evaluate a card transaction authorization assessment |
| ExBQ | Execute (112), Exchange (1), Request (1) | 114 | ATMNetworkOperations.yaml:351: ExBQ Execute an available automated action for Device Tracking |
| ExCR | Execute (74), Exchange (2) | 76 | ATMNetworkOperations.yaml:64: ExCR Execute an available automated action for ATM Network Operating S |
| GrBQ | Grant (8) | 8 | CardTerminalAdministration.yaml:244: GrBQ Obtain usage authorization grant for the device (may restrict usa |
| GrCR | Grant (38) | 38 | Advertising.yaml:272: GrCR Obtain a permission grant against the plan (e.g. obtain authority |
| InBQ | Initiate (200), Register (4) | 204 | ATMNetworkOperations.yaml:325: InBQ Instantiate a new Financial Transaction Capture |
| InCR | Initiate (105), Register (7) | 112 | ATMNetworkOperations.yaml:220: InCR Instantiate a new ATM Network Operating Session |
| PrBQ | Initiate (4), Provide (2), Request (1) | 7 | CardTerminalAdministration.yaml:88: PrBQ Provide/allocate the device to a merchant |
| PrCR | Provide (2), Initiate (1) | 3 | CardTerminalAdministration.yaml:64: PrCR Initial provision and registering of a point of sale (POS) device |
| ReBQ | Retrieve (521), Request (4), Register (1) | 526 | ATMNetworkOperations.yaml:484: ReBQ Retrieve details about any aspect of Cash Distribution |
| ReCR | Retrieve (175), Request (1) | 176 | ATMNetworkOperations.yaml:143: ReCR Retrieve details about any aspect of ATM Network Operating Sessio |
| RqBQ | Request (171) | 171 | ATMNetworkOperations.yaml:638: RqBQ Request manual intervention or a decision with respect to Cash Di |
| RqCR | Request (131) | 131 | ATMNetworkOperations.yaml:90: RqCR Request manual intervention or a decision with respect to ATM Net |
| RwBQ | Retrieve (1) | 1 | CustomerBilling.yaml:295: RwBQ Retrieve details about tracking and reminder activity |
| UpBQ | Update (400) | 400 | ATMNetworkOperations.yaml:559: UpBQ Update details relating to Financial Document Handling |
| UpCR | Update (160) | 160 | ATMNetworkOperations.yaml:167: UpCR Update details relating to ATM Network Operating Session |

## ATM Network Operations

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ATMNetworkOperations.yaml` (sha256 `8f7d6a479479…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: ATMNetworkOperations.yaml`
- **Purpose (verbatim from spec):** Handling the automated operation of the ATM network and linked devices, including tracing physical cash and document movements [ATMNetworkOperations.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`ATM` in title); Corporate Operations & Support (`Network` in title); Finance, Accounting & Treasury (`cash` in description) [ATMNetworkOperations.yaml:3]
- **Control Record:** ATMNetworkOperatingSession [ATMNetworkOperations.yaml:15]
- **Behavior Qualifiers (5):** CashDistribution [ATMNetworkOperations.yaml:119], NetworkOperation [ATMNetworkOperations.yaml:196], DeviceTracking [ATMNetworkOperations.yaml:247], FinancialDocumentHandling [ATMNetworkOperations.yaml:274], FinancialTransactionCapture [ATMNetworkOperations.yaml:301]
- **Operations (28):** Control 2, Exchange 5, Execute 4, Initiate 4, Request 2, Retrieve 6, Update 5 [ATMNetworkOperations.yaml:12]
- **Schemas:** 32 total, 7 domain-specific, 25 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `ATMNetworkOperatingSession/Created`) [asyncapi:ATMNetworkOperations.yaml:10]

## Account Reconciliation

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/AccountReconciliation.yaml` (sha256 `f4d975f6b43d…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: AccountReconciliation.yaml`
- **Purpose (verbatim from spec):** This Service Domain handles account reconciliation tasks [AccountReconciliation.yaml:4]
- **Theme [derived-rule]:** primary Deposits & Accounts; all matches: Deposits & Accounts (`Account` in title); Finance, Accounting & Treasury (`Reconcil` in title); Corporate Operations & Support (`Service` in description) [AccountReconciliation.yaml:3]
- **Control Record:** AccountReconciliationProcedure [AccountReconciliation.yaml:15]
- **Behavior Qualifiers (2):** AccountAssessment [AccountReconciliation.yaml:165], AccountResolution [AccountReconciliation.yaml:245]
- **Operations (22):** Control 1, Exchange 3, Execute 3, Initiate 3, Notify 3, Request 3, Retrieve 3, Update 3 [AccountReconciliation.yaml:12]
- **Schemas:** 129 total, 12 domain-specific, 117 shared-across-≥10-specs
- **Event channels:** 15 (e.g. `AccountReconciliationProcedure/Created`) [asyncapi:AccountReconciliation.yaml:9]

## Account Recovery

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/AccountRecovery.yaml` (sha256 `2e01765493eb…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: AccountRecovery.yaml`
- **Purpose (verbatim from spec):** This service domain handles the restructuring of a distressed account (loan) after standard recovery procedures have been exhausted [AccountRecovery.yaml:4]
- **Theme [derived-rule]:** primary Deposits & Accounts; all matches: Deposits & Accounts (`Account` in title); Lending & Credit (`loan` in description); Corporate Operations & Support (`service` in description) [AccountRecovery.yaml:3]
- **Control Record:** AccountRecoveryProcedure [AccountRecovery.yaml:177]
- **Behavior Qualifiers (5):** Writedown [AccountRecovery.yaml:15], Negotiation [AccountRecovery.yaml:42], Modification [AccountRecovery.yaml:69], Planning [AccountRecovery.yaml:123], Assessment [AccountRecovery.yaml:331]
- **Operations (17):** Exchange 4, Initiate 1, Request 1, Retrieve 5, Update 6 [AccountRecovery.yaml:12]
- **Schemas:** 126 total, 10 domain-specific, 116 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `AccountRecoveryProcedure/Created`) [asyncapi:AccountRecovery.yaml:10]

## Accounts Receivable

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/AccountsReceivable.yaml` (sha256 `56e4a9fe6cce…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: AccountsReceivable.yaml`
- **Purpose (verbatim from spec):** This service domain handles accounts receivable for invoices issue by the bank to customers and partners. It includes follow-up and resolution activity for delayed/missed payments [AccountsReceivable.yaml:4]
- **Theme [derived-rule]:** primary Deposits & Accounts; all matches: Deposits & Accounts (`Account` in title); Finance, Accounting & Treasury (`Receivable` in title); Payments & Settlement (`payment` in description); Customer, Sales & Marketing (`customer` in description); Channels & Servicing (`voice` in description); Corporate Operations & Support (`service` in description) [AccountsReceivable.yaml:3]
- **Control Record:** AccountsReceivableProcedure [AccountsReceivable.yaml:15]
- **Behavior Qualifiers (4):** Payment [AccountsReceivable.yaml:141], ReceivablesEvaluation [AccountsReceivable.yaml:167], Resolution [AccountsReceivable.yaml:194], CustomerNegotiation [AccountsReceivable.yaml:220]
- **Operations (22):** Control 1, Exchange 3, Execute 1, Initiate 5, Request 2, Retrieve 5, Update 5 [AccountsReceivable.yaml:12]
- **Schemas:** 83 total, 6 domain-specific, 77 shared-across-≥10-specs
- **Event channels:** 12 (e.g. `AccountsReceivableProcedure/Created`) [asyncapi:AccountsReceivable.yaml:11]

## Advanced Voice Services Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/AdvancedVoiceServicesManagement.yaml` (sha256 `f23e5cd82592…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: AdvancedVoiceServicesManagement.yaml`
- **Purpose (verbatim from spec):** Oversee the configuration and operation of the voice channel facilities [AdvancedVoiceServicesManagement.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Voice` in title); Corporate Operations & Support (`Service` in title) [AdvancedVoiceServicesManagement.yaml:3]
- **Control Record:** VoiceChannelManagementPlan [AdvancedVoiceServicesManagement.yaml:15]
- **Behavior Qualifiers (3):** MaintenanceAndUpgrades [AdvancedVoiceServicesManagement.yaml:141], CapacityPlanning [AdvancedVoiceServicesManagement.yaml:168], Troubleshooting [AdvancedVoiceServicesManagement.yaml:300]
- **Operations (15):** Create 2, Exchange 1, Request 4, Retrieve 4, Update 4 [AdvancedVoiceServicesManagement.yaml:12]
- **Schemas:** 52 total, 8 domain-specific, 44 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `VoiceChannelManagementPlan/Created`) [asyncapi:AdvancedVoiceServicesManagement.yaml:9]

## Advanced Voice Services Operations

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/AdvancedVoiceServicesOperations.yaml` (sha256 `fb7750bc6ee9…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: AdvancedVoiceServicesOperations.yaml`
- **Purpose (verbatim from spec):** This service domain operates the telephone channel infrastructure, including the IVR and any other automated devices as appropriate. This includes handling default routing rules and intra-day/session adjustments to deal with peak load or other operational variations [AdvancedVoiceServicesOperations.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Voice` in title); Corporate Operations & Support (`Service` in title) [AdvancedVoiceServicesOperations.yaml:3]
- **Control Record:** VoiceChannelOperatingSession [AdvancedVoiceServicesOperations.yaml:15]
- **Behavior Qualifiers (2):** Inbound [AdvancedVoiceServicesOperations.yaml:141], Outbound [AdvancedVoiceServicesOperations.yaml:192]
- **Operations (9):** Control 1, Initiate 3, Request 1, Retrieve 3, Update 1 [AdvancedVoiceServicesOperations.yaml:12]
- **Schemas:** 50 total, 9 domain-specific, 41 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `VoiceChannelOperatingSession/Created`) [asyncapi:AdvancedVoiceServicesOperations.yaml:12]

## Advertising

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/Advertising.yaml` (sha256 `6f8c4cfacd46…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: Advertising.yaml`
- **Purpose (verbatim from spec):** Develop the plan for and oversee advertising campaign activity, including budget and resource management [Advertising.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Advertis` in title); Finance, Accounting & Treasury (`budget` in description) [Advertising.yaml:3]
- **Control Record:** AdvertisingCampaignManagementPlan [Advertising.yaml:42]
- **Behavior Qualifiers (3):** MarketTracking [Advertising.yaml:15], PerformanceAssessment [Advertising.yaml:119], CampaignDirection [Advertising.yaml:145]
- **Operations (18):** Create 3, Execute 2, Grant 1, Request 4, Retrieve 4, Update 4 [Advertising.yaml:12]
- **Schemas:** 65 total, 10 domain-specific, 55 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `AdvertisingCampaignManagementPlan/Created`) [asyncapi:Advertising.yaml:10]

## Archive Services

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ArchiveServices.yaml` (sha256 `c79773d94afa…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: ArchiveServices.yaml`
- **Purpose (verbatim from spec):** The Archive Services Service Domain enables the bank to retain, maintain and access significant documents that are no longer actively accessed but that might be required in the future [ArchiveServices.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`Archive` in title) [ArchiveServices.yaml:3]
- **Control Record:** ArchiveOperatingSession [ArchiveServices.yaml:15]
- **Behavior Qualifiers (3):** DocumentMaintenance [ArchiveServices.yaml:217], DocumentCapture [ArchiveServices.yaml:269], DocumentRetrieval [ArchiveServices.yaml:323]
- **Operations (29):** Control 1, Exchange 4, Execute 4, Initiate 4, Notify 4, Request 4, Retrieve 4, Update 4 [ArchiveServices.yaml:12]
- **Schemas:** 38 total, 5 domain-specific, 33 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `ArchiveOperatingSession/Created`) [asyncapi:ArchiveServices.yaml:11]

## Asset And Liability Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/AssetAndLiabilityManagement.yaml` (sha256 `47d78bb8fb0f…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: AssetAndLiabilityManagement.yaml`
- **Purpose (verbatim from spec):** The unit overseeing the banks asset & liability policies and position [AssetAndLiabilityManagement.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`position` in description); Risk, Compliance & Fraud (`polic` in description) [AssetAndLiabilityManagement.yaml:4]
- **Control Record:** AssetAndLiabilityPortfolioStrategy [AssetAndLiabilityManagement.yaml:41]
- **Behavior Qualifiers (1):** TransactionAlignment [AssetAndLiabilityManagement.yaml:15]
- **Operations (8):** Create 1, Exchange 1, Grant 1, Request 2, Retrieve 2, Update 1 [AssetAndLiabilityManagement.yaml:12]
- **Schemas:** 51 total, 6 domain-specific, 45 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `AssetAndLiabilityPortfolioStrategy/Created`) [asyncapi:AssetAndLiabilityManagement.yaml:9]

## Asset Securitization

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/AssetSecuritization.yaml` (sha256 `af178edf02ea…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: AssetSecuritization.yaml`
- **Purpose (verbatim from spec):** Determine and select assets for securitization as needed to maintain and optimize the Bank's portfolio. Administer the securitization process [AssetSecuritization.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Securit` in title) [AssetSecuritization.yaml:3]
- **Control Record:** AssetSecuritizationTransaction [AssetSecuritization.yaml:15]
- **Behavior Qualifiers (3):** Placement [AssetSecuritization.yaml:93], Selection [AssetSecuritization.yaml:120], Securitization [AssetSecuritization.yaml:173]
- **Operations (22):** Control 1, Exchange 4, Execute 1, Initiate 4, Request 4, Retrieve 4, Update 4 [AssetSecuritization.yaml:12]
- **Schemas:** 131 total, 7 domain-specific, 124 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `AssetSecuritizationTransaction/Created`) [asyncapi:AssetSecuritization.yaml:10]

## Bank Drafts

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/BankDrafts.yaml` (sha256 `be9ff02920b2…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: BankDrafts.yaml`
- **Purpose (verbatim from spec):** This Service Domain support bank guaranteed payment transactions such as bank drafts [BankDrafts.yaml:4]
- **Theme [derived-rule]:** primary Payments & Settlement; all matches: Payments & Settlement (`payment` in description); Lending & Credit (`guarantee` in description); Corporate Operations & Support (`Service` in description) [BankDrafts.yaml:4]
- **Control Record:** BearerDocumentTransaction [BankDrafts.yaml:15]
- **Behavior Qualifiers (4):** BankGuaranteedPaymentRemittance [BankDrafts.yaml:191], CustomerPayment [BankDrafts.yaml:218], BearerDocumentCreationandRegistration [BankDrafts.yaml:272], BankGuaranteedPaymentSpecification [BankDrafts.yaml:325]
- **Operations (36):** Control 1, Exchange 5, Execute 5, Initiate 5, Notify 5, Request 5, Retrieve 5, Update 5 [BankDrafts.yaml:12]
- **Schemas:** 90 total, 12 domain-specific, 78 shared-across-≥10-specs
- **Event channels:** 17 (e.g. `BearerDocumentTransaction/Created`) [asyncapi:BankDrafts.yaml:9]

## Bank Guarantee

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/BankGuarantee.yaml` (sha256 `3a1f74db367e…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: BankGuarantee.yaml`
- **Purpose (verbatim from spec):** This Service Domain handles the pricing and issuance of a broad range of bank guarantee instruments [BankGuarantee.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Guarantee` in title); Reference & Data Management (`pricing` in description); Corporate Operations & Support (`Service` in description) [BankGuarantee.yaml:3]
- **Control Record:** BankGuaranteeTransaction [BankGuarantee.yaml:15]
- **Behavior Qualifiers (6):** Collection [BankGuarantee.yaml:217], BankGuaranteeDefinitionandPricing [BankGuarantee.yaml:244], CustomerPayment [BankGuarantee.yaml:325], BankGuaranteePayout [BankGuarantee.yaml:352], CustomerCollateralAllocation [BankGuarantee.yaml:431], BankGuaranteeIssuanceandBooking [BankGuarantee.yaml:485]
- **Operations (50):** Control 1, Exchange 7, Execute 7, Initiate 7, Notify 7, Request 7, Retrieve 7, Update 7 [BankGuarantee.yaml:12]
- **Schemas:** 120 total, 20 domain-specific, 100 shared-across-≥10-specs
- **Event channels:** 23 (e.g. `BankGuaranteeTransaction/Created`) [asyncapi:BankGuarantee.yaml:9]

## Branch Currency Distribution

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/BranchCurrencyDistribution.yaml` (sha256 `bf6ab29b7e54…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: BranchCurrencyDistribution.yaml`
- **Purpose (verbatim from spec):** Schedule and coordinate the secure distribution of cash inventory across the branch and ATM networks. [BranchCurrencyDistribution.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Branch` in title); Reference & Data Management (`Currency` in title); Finance, Accounting & Treasury (`cash` in description); Corporate Operations & Support (`network` in description) [BranchCurrencyDistribution.yaml:3]
- **Control Record:** CashDistributionProcedure [BranchCurrencyDistribution.yaml:15]
- **Behavior Qualifiers (4):** DistributionPlanning [BranchCurrencyDistribution.yaml:169], InventoryProvisioning [BranchCurrencyDistribution.yaml:220], InventoryDistributionOversight [BranchCurrencyDistribution.yaml:272], DistributionVehicleAdministration [BranchCurrencyDistribution.yaml:351]
- **Operations (21):** Control 1, Exchange 3, Execute 1, Initiate 1, Request 5, Retrieve 5, Update 5 [BranchCurrencyDistribution.yaml:12]
- **Schemas:** 79 total, 8 domain-specific, 71 shared-across-≥10-specs
- **Event channels:** 12 (e.g. `CashDistributionProcedure/Created`) [asyncapi:BranchCurrencyDistribution.yaml:9]

## Branch Currency Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/BranchCurrencyManagement.yaml` (sha256 `2800fb2ee386…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: BranchCurrencyManagement.yaml`
- **Purpose (verbatim from spec):** Track cash inventory, project demand and ensure all cash is accounted for within the branch [BranchCurrencyManagement.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Branch` in title); Reference & Data Management (`Currency` in title); Deposits & Accounts (`account` in description); Finance, Accounting & Treasury (`cash` in description); Corporate Operations & Support (`project` in description) [BranchCurrencyManagement.yaml:3]
- **Control Record:** BranchCashAllocation [BranchCurrencyManagement.yaml:15]
- **Behavior Qualifiers (1):** InventoryAllocation [BranchCurrencyManagement.yaml:143]
- **Operations (12):** Capture 2, Control 2, Exchange 2, Initiate 2, Retrieve 2, Update 2 [BranchCurrencyManagement.yaml:12]
- **Schemas:** 65 total, 4 domain-specific, 61 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `BranchCashAllocation/Created`) [asyncapi:BranchCurrencyManagement.yaml:9]

## Branch Location Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/BranchLocationManagement.yaml` (sha256 `931a5673221b…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: BranchLocationManagement.yaml`
- **Purpose (verbatim from spec):** Manage and oversee branch activity, assign resources to optimize branch performance [BranchLocationManagement.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Branch` in title) [BranchLocationManagement.yaml:3]
- **Control Record:** BranchLocationManagementPlan [BranchLocationManagement.yaml:15]
- **Behavior Qualifiers (4):** ProductandServicePlanning [BranchLocationManagement.yaml:219], CustomerLiaison [BranchLocationManagement.yaml:246], StaffandLocationPlanning [BranchLocationManagement.yaml:273], Troubleshooting [BranchLocationManagement.yaml:300]
- **Operations (27):** Capture 5, Control 2, Exchange 1, Grant 1, Initiate 3, Request 5, Retrieve 5, Update 5 [BranchLocationManagement.yaml:12]
- **Schemas:** 56 total, 8 domain-specific, 48 shared-across-≥10-specs
- **Event channels:** 12 (e.g. `BranchLocationManagementPlan/Created`) [asyncapi:BranchLocationManagement.yaml:9]

## Branch Location Operations

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/BranchLocationOperations.yaml` (sha256 `75f1a8da82d2…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: BranchLocationOperations.yaml`
- **Purpose (verbatim from spec):** The day to day administration of branch activity, including teller assignment and cash handling oversight [BranchLocationOperations.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Branch` in title); Finance, Accounting & Treasury (`cash` in description) [BranchLocationOperations.yaml:3]
- **Control Record:** BranchLocationAdministrativePlan [BranchLocationOperations.yaml:15]
- **Behavior Qualifiers (1):** CashInventoryHandling [BranchLocationOperations.yaml:191]
- **Operations (14):** Control 1, Create 1, Exchange 2, Grant 2, Notify 2, Request 2, Retrieve 2, Update 2 [BranchLocationOperations.yaml:12]
- **Schemas:** 75 total, 9 domain-specific, 66 shared-across-≥10-specs
- **Event channels:** 18 (e.g. `BranchLocationAdministrativePlan/Created`) [asyncapi:BranchLocationOperations.yaml:10]

## Brand Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/BrandManagement.yaml` (sha256 `67b254d173fa…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: BrandManagement.yaml`
- **Purpose (verbatim from spec):** Respond to events that potentially damage the brand or provide an opportunity to strengthen/leverage brand awareness [BrandManagement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Brand` in title) [BrandManagement.yaml:3]
- **Control Record:** BrandManagementPlan [BrandManagement.yaml:15]
- **Behavior Qualifiers (2):** BrandAdvice [BrandManagement.yaml:41], Troubleshooting [BrandManagement.yaml:249]
- **Operations (13):** Create 2, Exchange 1, Grant 1, Request 3, Retrieve 3, Update 3 [BrandManagement.yaml:12]
- **Schemas:** 28 total, 4 domain-specific, 24 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `BrandManagementPlan/Created`) [asyncapi:BrandManagement.yaml:10]

## Brokered Product Proxy

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/BrokeredProductProxy.yaml` (sha256 `c0b8b87830d9…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: BrokeredProductProxy.yaml`
- **Purpose (verbatim from spec):** This Service Domain oversees all activities associated with the coordinated delivery of 3rd party products and services [BrokeredProductProxy.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Broker` in title); Customer, Sales & Marketing (`Product` in title); Corporate Operations & Support (`Service` in description) [BrokeredProductProxy.yaml:3]
- **Behavior Qualifiers:** none
- **Operations:** none defined (the OpenAPI `paths` section is empty or absent)
- **Schemas:** 3 total, 2 domain-specific, 1 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `BrokeredProductFacility/Created`) [asyncapi:BrokeredProductProxy.yaml:10]

## Business Development

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/BusinessDevelopment.yaml` (sha256 `f3d00afae52f…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: BusinessDevelopment.yaml`
- **Purpose (verbatim from spec):** Define, implement, track and assess the new business development plans [BusinessDevelopment.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`Business` in title) [BusinessDevelopment.yaml:3]
- **Control Record:** BusinessDevelopmentStrategy [BusinessDevelopment.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (7):** Capture 1, Create 1, Exchange 1, Grant 1, Request 1, Retrieve 1, Update 1 [BusinessDevelopment.yaml:12]
- **Schemas:** 82 total, 23 domain-specific, 59 shared-across-≥10-specs
- **Event channels:** 18 (e.g. `BusinessDevelopmentStrategy/Created`) [asyncapi:BusinessDevelopment.yaml:9]

## Business Unit Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/BusinessUnitManagement.yaml` (sha256 `f6598dbb6320…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: BusinessUnitManagement.yaml`
- **Purpose (verbatim from spec):** Track and report on business unit activity and financial performance [BusinessUnitManagement.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`Business` in title); Finance, Accounting & Treasury (`financial` in description); Reference & Data Management (`report` in description) [BusinessUnitManagement.yaml:3]
- **Control Record:** BusinessUnitManagementPlan [BusinessUnitManagement.yaml:15]
- **Behavior Qualifiers (2):** Troubleshooting [BusinessUnitManagement.yaml:141], Performance [BusinessUnitManagement.yaml:167]
- **Operations (12):** Create 2, Exchange 1, Request 3, Retrieve 3, Update 3 [BusinessUnitManagement.yaml:12]
- **Schemas:** 40 total, 6 domain-specific, 34 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `BusinessUnitManagementPlan/Created`) [asyncapi:BusinessUnitManagement.yaml:9]

## Card Authorization

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CardAuthorization.yaml` (sha256 `c14889a9baf9…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: CardAuthorization.yaml`
- **Purpose (verbatim from spec):** This service domain is responsible for the real time card authorization decisions for credit/charge cards. [CardAuthorization.yaml:4]
- **Theme [derived-rule]:** primary Cards & Merchant Services; all matches: Cards & Merchant Services (`Card` in title); Lending & Credit (`credit` in description); Corporate Operations & Support (`service` in description) [CardAuthorization.yaml:3]
- **Control Record:** CreditCardAuthorizationAssessment [CardAuthorization.yaml:15]
- **Behavior Qualifiers (6):** DeviceCheck [CardAuthorization.yaml:219], Authentication [CardAuthorization.yaml:271], FraudCheck [CardAuthorization.yaml:296], CreditCheck [CardAuthorization.yaml:321], StandIn [CardAuthorization.yaml:373], Authorization [CardAuthorization.yaml:398]
- **Operations (16):** Control 1, Evaluate 2, Exchange 1, Execute 1, Grant 1, Request 1, Retrieve 6, Update 3 [CardAuthorization.yaml:12]
- **Schemas:** 174 total, 22 domain-specific, 152 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `CreditCardAuthorizationAssessment/Created`) [asyncapi:CardAuthorization.yaml:10]

## Card Case

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CardCase.yaml` (sha256 `7709303634c7…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: CardCase.yaml`
- **Purpose (verbatim from spec):** This service domain handles the processing of a customer card case, typically a disputed charge [CardCase.yaml:4]
- **Theme [derived-rule]:** primary Cards & Merchant Services; all matches: Cards & Merchant Services (`Card` in title); Channels & Servicing (`Case` in title); Customer, Sales & Marketing (`customer` in description); Corporate Operations & Support (`service` in description) [CardCase.yaml:3]
- **Control Record:** CardCaseProcedure [CardCase.yaml:15]
- **Behavior Qualifiers (4):** Consolidation [CardCase.yaml:143], Chargeback [CardCase.yaml:245], Arbitration [CardCase.yaml:297], Resolution [CardCase.yaml:376]
- **Operations (17):** Control 1, Exchange 3, Execute 1, Initiate 1, Request 1, Retrieve 5, Update 5 [CardCase.yaml:12]
- **Schemas:** 178 total, 16 domain-specific, 162 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `CardCaseProcedure/Created`) [asyncapi:CardCase.yaml:9]

## Card Clearing

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CardClearing.yaml` (sha256 `9d3a12878beb…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: CardClearing.yaml`
- **Purpose (verbatim from spec):** This service domain orchestrates the capture and consolidation of card financial transactions originating from various sources, such as POS Network, E-Commerce Gateway, ATM Network, or Card Case Management. It also handles the clearing of the transactions from the Acquirers to the Issuers through t… [CardClearing.yaml:4]
- **Theme [derived-rule]:** primary Payments & Settlement; all matches: Payments & Settlement (`Clearing` in title); Cards & Merchant Services (`Card` in title); Channels & Servicing (`ATM` in description); Finance, Accounting & Treasury (`financial` in description); Corporate Operations & Support (`service` in description) [CardClearing.yaml:3]
- **Control Record:** CardClearingProcedure [CardClearing.yaml:15]
- **Behavior Qualifiers (7):** Capture [CardClearing.yaml:89], Addressing [CardClearing.yaml:141], FXConversion [CardClearing.yaml:166], Charge [CardClearing.yaml:191], Matching [CardClearing.yaml:243], Reconciliation [CardClearing.yaml:268], Routing [CardClearing.yaml:293]
- **Operations (13):** Execute 1, Initiate 1, Retrieve 8, Update 3 [CardClearing.yaml:12]
- **Schemas:** 156 total, 17 domain-specific, 139 shared-across-≥10-specs
- **Event channels:** 16 (e.g. `CardClearingProcedure/Created`) [asyncapi:CardClearing.yaml:12]
- **Other domains named in this purpose text:** Card Case [CardClearing.yaml:4]

## Card Collections

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CardCollections.yaml` (sha256 `8a3365d9a7f7…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: CardCollections.yaml`
- **Purpose (verbatim from spec):** This service domain administers the recovery of outstanding amounts from cancelled card accounts through internal or external collection agencies. This may involve negotiating payment terms and/or interest write-downs. [CardCollections.yaml:4]
- **Theme [derived-rule]:** primary Cards & Merchant Services; all matches: Cards & Merchant Services (`Card` in title); Payments & Settlement (`payment` in description); Deposits & Accounts (`account` in description); Corporate Operations & Support (`service` in description) [CardCollections.yaml:3]
- **Control Record:** CardCollectionsProcedure [CardCollections.yaml:15]
- **Behavior Qualifiers (4):** Assignment [CardCollections.yaml:167], PaymentTerms [CardCollections.yaml:192], Payment [CardCollections.yaml:244], Resolution [CardCollections.yaml:349]
- **Operations (16):** Control 1, Exchange 2, Execute 1, Initiate 2, Request 1, Retrieve 5, Update 4 [CardCollections.yaml:12]
- **Schemas:** 190 total, 9 domain-specific, 181 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `CardCollectionsProcedure/Created`) [asyncapi:CardCollections.yaml:11]

## Card Financial Settlement

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CardFinancialSettlement.yaml` (sha256 `d2b6b7e395fd…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: CardFinancialSettlement.yaml`
- **Purpose (verbatim from spec):** This service domain orchestrates the settlement of the transactions between the Issuers and the Acquirers through the Card Networks. [CardFinancialSettlement.yaml:4]
- **Theme [derived-rule]:** primary Payments & Settlement; all matches: Payments & Settlement (`Settle` in title); Cards & Merchant Services (`Card` in title); Finance, Accounting & Treasury (`Financial` in title); Corporate Operations & Support (`service` in description) [CardFinancialSettlement.yaml:3]
- **Control Record:** CardFinancialSettlementProcedure [CardFinancialSettlement.yaml:15]
- **Behavior Qualifiers (4):** Consolidation [CardFinancialSettlement.yaml:65], Processing [CardFinancialSettlement.yaml:167], Payment [CardFinancialSettlement.yaml:192], Instruction [CardFinancialSettlement.yaml:246]
- **Operations (12):** Control 1, Initiate 1, Retrieve 5, Update 5 [CardFinancialSettlement.yaml:12]
- **Schemas:** 86 total, 9 domain-specific, 77 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `CardFinancialSettlementProcedure/Created`) [asyncapi:CardFinancialSettlement.yaml:10]

## Card Network Participant Facility

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CardNetworkParticipantFacility.yaml` (sha256 `c47486a2466b…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: CardNetworkParticipantFacility.yaml`
- **Purpose (verbatim from spec):** This service domain orchestrates the activities related to the inclusion of new Acquirers and Issuers in the Card Network, their terms and conditions and their status. [CardNetworkParticipantFacility.yaml:4]
- **Theme [derived-rule]:** primary Cards & Merchant Services; all matches: Cards & Merchant Services (`Card` in title); Corporate Operations & Support (`Network` in title) [CardNetworkParticipantFacility.yaml:3]
- **Control Record:** CardNetworkParticipantAgreement [CardNetworkParticipantFacility.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (4):** Control 1, Initiate 1, Retrieve 1, Update 1 [CardNetworkParticipantFacility.yaml:12]
- **Schemas:** 40 total, 2 domain-specific, 38 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `CardNetworkParticipantAgreement/Created`) [asyncapi:CardNetworkParticipantFacility.yaml:10]

## Card Terminal Administration

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CardTerminalAdministration.yaml` (sha256 `86b6c5703dc0…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: CardTerminalAdministration.yaml`
- **Purpose (verbatim from spec):** This service domain administers the POS Network including the inventory, terminal characteristics, deployment and status of the POS devices. [CardTerminalAdministration.yaml:4]
- **Theme [derived-rule]:** primary Cards & Merchant Services; all matches: Cards & Merchant Services (`Card` in title); Corporate Operations & Support (`service` in description) [CardTerminalAdministration.yaml:3]
- **Control Record:** CardPOSDeviceAllocation [CardTerminalAdministration.yaml:15]
- **Behavior Qualifiers (1):** Allocation [CardTerminalAdministration.yaml:91]
- **Operations (11):** Capture 1, Control 1, Exchange 1, Grant 1, Provide 2, Request 1, Retrieve 2, Update 2 [CardTerminalAdministration.yaml:12]
- **Schemas:** 99 total, 4 domain-specific, 95 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `CardPOSDeviceAllocation/Created`) [asyncapi:CardTerminalAdministration.yaml:10]

## Card Terminal Operation

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CardTerminalOperation.yaml` (sha256 `b656badbae3e…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: CardTerminalOperation.yaml`
- **Purpose (verbatim from spec):** This service domain handle POS operations including processing, capture and tracking of the transactions originating at the Point of Sale devices. [CardTerminalOperation.yaml:4]
- **Theme [derived-rule]:** primary Cards & Merchant Services; all matches: Cards & Merchant Services (`Card` in title); Corporate Operations & Support (`service` in description) [CardTerminalOperation.yaml:3]
- **Control Record:** CardPOSNetworkOperatingSession [CardTerminalOperation.yaml:15]
- **Behavior Qualifiers (3):** Capture [CardTerminalOperation.yaml:115], Authorization [CardTerminalOperation.yaml:195], Batch [CardTerminalOperation.yaml:246]
- **Operations (15):** Control 1, Initiate 4, Request 3, Retrieve 4, Update 3 [CardTerminalOperation.yaml:12]
- **Schemas:** 130 total, 6 domain-specific, 124 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `CardPOSNetworkOperatingSession/Created`) [asyncapi:CardTerminalOperation.yaml:10]

## Card Transaction Capture

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CardTransactionCapture.yaml` (sha256 `39bc9500c3de…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: CardTransactionCapture.yaml`
- **Purpose (verbatim from spec):** A distributed facility to capture card transactions at the point of sale [CardTransactionCapture.yaml:4]
- **Theme [derived-rule]:** primary Cards & Merchant Services; all matches: Cards & Merchant Services (`Card` in title); Corporate Operations & Support (`facilit` in description) [CardTransactionCapture.yaml:3]
- **Control Record:** CardFinancialCaptureTransaction [CardTransactionCapture.yaml:15]
- **Behavior Qualifiers (4):** TransactionConsolidation [CardTransactionCapture.yaml:193], TransactionAuthorization [CardTransactionCapture.yaml:274], TransactionCapture [CardTransactionCapture.yaml:300], TransactionReversal [CardTransactionCapture.yaml:402]
- **Operations (22):** Control 2, Exchange 2, Execute 2, Initiate 5, Request 1, Retrieve 5, Update 5 [CardTransactionCapture.yaml:12]
- **Schemas:** 132 total, 8 domain-specific, 124 shared-across-≥10-specs
- **Event channels:** 12 (e.g. `CardFinancialCaptureTransaction/Created`) [asyncapi:CardTransactionCapture.yaml:9]

## Card Transaction Switch

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CardTransactionSwitch.yaml` (sha256 `86716024f9ef…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: CardTransactionSwitch.yaml`
- **Purpose (verbatim from spec):** This service domain orchestrates the switching and routing of Card Authorization and Financial transactions received through the Card POS Network, Card E-Commerce Gateway, or the ATM Network from the Acquirer to the Issuer through the Card Networks. [CardTransactionSwitch.yaml:4]
- **Theme [derived-rule]:** primary Cards & Merchant Services; all matches: Cards & Merchant Services (`Card` in title); Channels & Servicing (`ATM` in description); Finance, Accounting & Treasury (`Financial` in description); Corporate Operations & Support (`service` in description) [CardTransactionSwitch.yaml:3]
- **Control Record:** CardTransactionSwitchOperatingSession [CardTransactionSwitch.yaml:15]
- **Behavior Qualifiers (1):** TransactionCapture [CardTransactionSwitch.yaml:141]
- **Operations (7):** Control 1, Exchange 1, Initiate 2, Retrieve 2, Update 1 [CardTransactionSwitch.yaml:12]
- **Schemas:** 141 total, 6 domain-specific, 135 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `CardTransactionSwitchOperatingSession/Created`) [asyncapi:CardTransactionSwitch.yaml:12]
- **Other domains named in this purpose text:** Card Authorization [CardTransactionSwitch.yaml:4]

## Card Transaction Tracking

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CardTransactionTracking.yaml` (sha256 `c29e3f625019…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: CardTransactionTracking.yaml`
- **Purpose (verbatim from spec):** Maintain a log of credit card bookings and authorizations for operational and management information, tracking and reconciliation purposes. [CardTransactionTracking.yaml:4]
- **Theme [derived-rule]:** primary Cards & Merchant Services; all matches: Cards & Merchant Services (`Card` in title); Lending & Credit (`credit` in description); Finance, Accounting & Treasury (`reconcil` in description); Reference & Data Management (`information` in description) [CardTransactionTracking.yaml:3]
- **Behavior Qualifiers:** none
- **Operations:** none defined (the OpenAPI `paths` section is empty or absent)
- **Schemas:** 4 total, 3 domain-specific, 1 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `CreditCardPositionLog/Created`) [asyncapi:CardTransactionTracking.yaml:10]
- **Other domains named in this purpose text:** Credit Card [CardTransactionTracking.yaml:4]

## Card eCommerce Gateway

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CardeCommerceGateway.yaml` (sha256 `ced15a0bb18a…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: CardeCommerceGateway.yaml`
- **Purpose (verbatim from spec):** This service domain orchestrates the processing of e-commerce transactions for authentication, authorization and capture of the financial transactions. [CardeCommerceGateway.yaml:4]
- **Theme [derived-rule]:** primary Cards & Merchant Services; all matches: Cards & Merchant Services (`Card` in title); Finance, Accounting & Treasury (`financial` in description); Corporate Operations & Support (`service` in description) [CardeCommerceGateway.yaml:3]
- **Control Record:** eCommerceGatewayOperatingSession [CardeCommerceGateway.yaml:15]
- **Behavior Qualifiers (4):** CardPayment [CardeCommerceGateway.yaml:41], TransactionBatch [CardeCommerceGateway.yaml:91], CardAuthentication [CardeCommerceGateway.yaml:221], TransactionAuthorization [CardeCommerceGateway.yaml:299]
- **Operations (14):** Control 1, Initiate 4, Retrieve 5, Update 4 [CardeCommerceGateway.yaml:12]
- **Schemas:** 99 total, 11 domain-specific, 88 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `eCommerceGatewayOperatingSession/Created`) [asyncapi:CardeCommerceGateway.yaml:10]

## Case Root Cause Analysis

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CaseRootCauseAnalysis.yaml` (sha256 `6ed2c859ead4…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: CaseRootCauseAnalysis.yaml`
- **Purpose (verbatim from spec):** Root cause analysis business function reviews case reports to identify possible improvements to eliminate/mitigate servicing issues [CaseRootCauseAnalysis.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Case` in title); Reference & Data Management (`report` in description); Corporate Operations & Support (`business` in description) [CaseRootCauseAnalysis.yaml:3]
- **Control Record:** CustomerCaseRootCauseAnalysis [CaseRootCauseAnalysis.yaml:15]
- **Behavior Qualifiers (3):** CreditandFraudRelatedIssueAnalysis [CaseRootCauseAnalysis.yaml:141], OperationsandServicingIssueAnalysis [CaseRootCauseAnalysis.yaml:168], ProductandServiceIssueAnalysis [CaseRootCauseAnalysis.yaml:195]
- **Operations (20):** Execute 4, Initiate 4, Request 4, Retrieve 4, Update 4 [CaseRootCauseAnalysis.yaml:12]
- **Schemas:** 34 total, 5 domain-specific, 29 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `CustomerCaseRootCauseAnalysis/Created`) [asyncapi:CaseRootCauseAnalysis.yaml:10]

## Cash Concentration

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CashConcentration.yaml` (sha256 `a51708540746…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: CashConcentration.yaml`
- **Purpose (verbatim from spec):** Cash Concentration is a cash management service aimed at moving a balance, or part of a balance of an account to a different account to meet various requirements. [CashConcentration.yaml:4]
- **Theme [derived-rule]:** primary Finance, Accounting & Treasury; all matches: Finance, Accounting & Treasury (`Cash` in title); Deposits & Accounts (`balance` in description); Corporate Operations & Support (`service` in description) [CashConcentration.yaml:3]
- **Control Record:** AccountBalanceSweepingFacility [CashConcentration.yaml:15]
- **Behavior Qualifiers (1):** CashTransfer [CashConcentration.yaml:241]
- **Operations (16):** Activate 1, Control 1, Exchange 2, Execute 2, Initiate 2, Notify 2, Request 2, Retrieve 2, Update 2 [CashConcentration.yaml:12]
- **Schemas:** 122 total, 3 domain-specific, 119 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `AccountBalanceSweepingFacility/Created`) [asyncapi:CashConcentration.yaml:10]

## Cash Management And Account Services

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CashManagementAndAccountServices.yaml` (sha256 `dd70600a6dc1…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: CashManagementAndAccountServices.yaml`
- **Purpose (verbatim from spec):** This service domain orchestrates a cash management and accounting services facility typically used by corporations to support additional cash management features over and above the standard facilities of current and savings accounts [CashManagementAndAccountServices.yaml:4]
- **Theme [derived-rule]:** primary Deposits & Accounts; all matches: Deposits & Accounts (`Account` in title); Finance, Accounting & Treasury (`Cash` in title); Corporate Operations & Support (`Service` in title) [CashManagementAndAccountServices.yaml:3]
- **Control Record:** CashManagementAndAccountServicesFacility [CashManagementAndAccountServices.yaml:15]
- **Behavior Qualifiers (9):** Interest [CashManagementAndAccountServices.yaml:91], Charge [CashManagementAndAccountServices.yaml:140], Sweep [CashManagementAndAccountServices.yaml:218], DebitandCredit [CashManagementAndAccountServices.yaml:269], Payment [CashManagementAndAccountServices.yaml:428], IssuedDevice [CashManagementAndAccountServices.yaml:560], PositivePay [CashManagementAndAccountServices.yaml:640], Deposit [CashManagementAndAccountServices.yaml:690], AmountBlock [CashManagementAndAccountServices.yaml:770]
- **Operations (34):** Control 1, Exchange 2, Execute 5, Initiate 8, Request 1, Retrieve 10, Update 7 [CashManagementAndAccountServices.yaml:12]
- **Schemas:** 221 total, 20 domain-specific, 201 shared-across-≥10-specs
- **Event channels:** 20 (e.g. `CashManagementAndAccountServicesFacility/Created`) [asyncapi:CashManagementAndAccountServices.yaml:11]

## Central Cash Handling

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CentralCashHandling.yaml` (sha256 `e723ec8b6468…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: CentralCashHandling.yaml`
- **Purpose (verbatim from spec):** Track cash inventory, project demand and allocate inventory across the branch/ATM network [CentralCashHandling.yaml:4]
- **Theme [derived-rule]:** primary Finance, Accounting & Treasury; all matches: Finance, Accounting & Treasury (`Cash` in title); Channels & Servicing (`branch` in description); Corporate Operations & Support (`project` in description) [CentralCashHandling.yaml:3]
- **Control Record:** CentralCashAllocation [CentralCashHandling.yaml:15]
- **Behavior Qualifiers (2):** ProjectionandAllocation [CentralCashHandling.yaml:167], TrackingandAllocation [CentralCashHandling.yaml:194]
- **Operations (18):** Capture 3, Control 3, Exchange 3, Initiate 3, Retrieve 3, Update 3 [CentralCashHandling.yaml:12]
- **Schemas:** 67 total, 6 domain-specific, 61 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `CentralCashAllocation/Created`) [asyncapi:CentralCashHandling.yaml:9]

## Channel Activity Analysis

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ChannelActivityAnalysis.yaml` (sha256 `a65a09976d83…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: ChannelActivityAnalysis.yaml`
- **Purpose (verbatim from spec):** This service domain tracks and analyzes channel activity to support relationship development, to detect unwanted behavior, possible fraud, and to constrain channel use as necessary (for example tracking usage frequency and cumulative transaction amounts within a period) [ChannelActivityAnalysis.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Channel` in title); Risk, Compliance & Fraud (`fraud` in description); Customer, Sales & Marketing (`relationship` in description); Corporate Operations & Support (`service` in description) [ChannelActivityAnalysis.yaml:3]
- **Control Record:** ChannelActivityAnalysis [ChannelActivityAnalysis.yaml:15]
- **Behavior Qualifiers (6):** CustomerFraud [ChannelActivityAnalysis.yaml:115], MerchantFraud [ChannelActivityAnalysis.yaml:167], MerchantBehavior [ChannelActivityAnalysis.yaml:219], CustomerBehavior [ChannelActivityAnalysis.yaml:244], Bot [ChannelActivityAnalysis.yaml:298], DeviceError [ChannelActivityAnalysis.yaml:350]
- **Operations (16):** Evaluate 1, Exchange 1, Execute 6, Request 1, Retrieve 7 [ChannelActivityAnalysis.yaml:12]
- **Schemas:** 17 total, 8 domain-specific, 9 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `ChannelActivityAnalysis/Created`) [asyncapi:ChannelActivityAnalysis.yaml:12]

## Channel Activity History

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ChannelActivityHistory.yaml` (sha256 `c4bc2129cca1…`, version 14.0.0); bundle: `oas3_yamls_part1.md` under `# FILE: ChannelActivityHistory.yaml`
- **Purpose (verbatim from spec):** This service domains consolidates and captures customer channel usage activity to support channel activity analysis and also can be referenced for customer access authorization and routing decisions [ChannelActivityHistory.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Channel` in title); Customer, Sales & Marketing (`customer` in description); Reference & Data Management (`reference` in description); Corporate Operations & Support (`service` in description) [ChannelActivityHistory.yaml:3]
- **Control Record:** ChannelActivityLog [ChannelActivityHistory.yaml:15]
- **Behavior Qualifiers (1):** Event [ChannelActivityHistory.yaml:115]
- **Operations (7):** Capture 1, Control 1, Initiate 1, Retrieve 2, Update 2 [ChannelActivityHistory.yaml:12]
- **Schemas:** 69 total, 9 domain-specific, 60 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `ChannelActivityLog/Created`) [asyncapi:ChannelActivityHistory.yaml:11]
- **Other domains named in this purpose text:** Channel Activity Analysis [ChannelActivityHistory.yaml:4]

## Cheque Lock Box

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ChequeLockBox.yaml` (sha256 `5e9e3b58c5a6…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: ChequeLockBox.yaml`
- **Purpose (verbatim from spec):** This Service Domain support paper cheque processing services offered to corporate customers [ChequeLockBox.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`customer` in description); Corporate Operations & Support (`Service` in description) [ChequeLockBox.yaml:4]
- **Control Record:** LockBoxFacility [ChequeLockBox.yaml:15]
- **Behavior Qualifiers (3):** IssueResolution [ChequeLockBox.yaml:191], Payment [ChequeLockBox.yaml:271], TransactionBatch [ChequeLockBox.yaml:325]
- **Operations (25):** Control 1, Exchange 3, Execute 3, Initiate 4, Notify 3, Request 3, Retrieve 4, Update 4 [ChequeLockBox.yaml:12]
- **Schemas:** 132 total, 6 domain-specific, 126 shared-across-≥10-specs
- **Event channels:** 13 (e.g. `LockBoxFacility/Created`) [asyncapi:ChequeLockBox.yaml:9]
- **Other domains named in this purpose text:** Cheque Processing [ChequeLockBox.yaml:4]

## Cheque Processing

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ChequeProcessing.yaml` (sha256 `922d1aee3e62…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: ChequeProcessing.yaml`
- **Purpose (verbatim from spec):** Handle the processing of paper cheques, generating financial transactions for processing [ChequeProcessing.yaml:4]
- **Theme [derived-rule]:** primary Finance, Accounting & Treasury; all matches: Finance, Accounting & Treasury (`financial` in description) [ChequeProcessing.yaml:4]
- **Control Record:** ChequeProcessingOperatingSession [ChequeProcessing.yaml:15]
- **Behavior Qualifiers (3):** FinancialTransactionInitiation [ChequeProcessing.yaml:193], ChequeExceptionHandling [ChequeProcessing.yaml:220], ChequeExtraction [ChequeProcessing.yaml:245]
- **Operations (13):** Control 1, Exchange 2, Execute 1, Initiate 2, Request 1, Retrieve 4, Update 2 [ChequeProcessing.yaml:12]
- **Schemas:** 37 total, 5 domain-specific, 32 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `ChequeProcessingOperatingSession/Created`) [asyncapi:ChequeProcessing.yaml:9]

## Claim Administration

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ClaimAdministration.yaml` (sha256 `917f0f4ced6a…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: ClaimAdministration.yaml`
- **Purpose (verbatim from spec):** The claim administration Service Domain implements the payment and support obligations of the policy in respect to a verified claim [ClaimAdministration.yaml:4]
- **Theme [derived-rule]:** primary Payments & Settlement; all matches: Payments & Settlement (`payment` in description); Risk, Compliance & Fraud (`polic` in description); Corporate Operations & Support (`Service` in description) [ClaimAdministration.yaml:4]
- **Behavior Qualifiers:** none
- **Operations:** none defined (the OpenAPI `paths` section is empty or absent)
- **Schemas:** 7 total, 6 domain-specific, 1 shared-across-≥10-specs
- **Event channels:** 12 (e.g. `ClaimProcessingAdministrativePlan/Created`) [asyncapi:ClaimAdministration.yaml:10]

## Claim Assessment

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ClaimAssessment.yaml` (sha256 `ee6ced1f1485…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: ClaimAssessment.yaml`
- **Purpose (verbatim from spec):** The Claim Assessment Service Domain runs through the required tests to confirm the veracity of a claim made under an insurance policy. [ClaimAssessment.yaml:4]
- **Theme [derived-rule]:** primary Risk, Compliance & Fraud; all matches: Risk, Compliance & Fraud (`polic` in description); Corporate Operations & Support (`Service` in description) [ClaimAssessment.yaml:4]
- **Behavior Qualifiers:** none
- **Operations:** none defined (the OpenAPI `paths` section is empty or absent)
- **Schemas:** 6 total, 5 domain-specific, 1 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `ClaimValidationAssessment/Created`) [asyncapi:ClaimAssessment.yaml:10]

## Collateral Allocation Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CollateralAllocationManagement.yaml` (sha256 `3ae6321c156c…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CollateralAllocationManagement.yaml`
- **Purpose (verbatim from spec):** The Service Domain manages the allocation of party owned assets to bank issued lending and other asset products. [CollateralAllocationManagement.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Collateral` in title); Customer, Sales & Marketing (`party` in description); Corporate Operations & Support (`Service` in description) [CollateralAllocationManagement.yaml:3]
- **Control Record:** CollateralAssetAllocation [CollateralAllocationManagement.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (4):** Capture 1, Exchange 1, Retrieve 1, Update 1 [CollateralAllocationManagement.yaml:12]
- **Schemas:** 23 total, 4 domain-specific, 19 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `CollateralAssetAllocation/Created`) [asyncapi:CollateralAllocationManagement.yaml:10]

## Collateral Asset Administration

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CollateralAssetAdministration.yaml` (sha256 `b8e940a0c33a…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CollateralAssetAdministration.yaml`
- **Purpose (verbatim from spec):** This service domain maintains the status of a customers collateral assets, including scheduled and ad-hoc valuations and confirmation of the correct completion of scheduled maintenance tasks. [CollateralAssetAdministration.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Collateral` in title); Customer, Sales & Marketing (`customer` in description); Corporate Operations & Support (`service` in description) [CollateralAssetAdministration.yaml:3]
- **Control Record:** CollateralAssetAdministrativePlan [CollateralAssetAdministration.yaml:15]
- **Behavior Qualifiers (2):** Valuation [CollateralAssetAdministration.yaml:89], Maintenance [CollateralAssetAdministration.yaml:194]
- **Operations (12):** Create 3, Exchange 1, Request 2, Retrieve 3, Update 3 [CollateralAssetAdministration.yaml:12]
- **Schemas:** 116 total, 6 domain-specific, 110 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `CollateralAssetAdministrativePlan/Created`) [asyncapi:CollateralAssetAdministration.yaml:11]

## Collections

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/Collections.yaml` (sha256 `6647a237c8cf…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: Collections.yaml`
- **Purpose (verbatim from spec):** Handles the liquidation of assets to offset the losses for problem accounts [Collections.yaml:4]
- **Theme [derived-rule]:** primary Deposits & Accounts; all matches: Deposits & Accounts (`account` in description) [Collections.yaml:4]
- **Control Record:** CollateralAssetLiquidationProcedure [Collections.yaml:15]
- **Behavior Qualifiers (5):** CollateralValuation [Collections.yaml:141], CollateralLiquidation [Collections.yaml:194], DebtFactoring [Collections.yaml:220], CollectionsAssessment [Collections.yaml:272], CollectionsAccountUpdate [Collections.yaml:428]
- **Operations (24):** Control 1, Exchange 4, Execute 1, Initiate 5, Request 1, Retrieve 6, Update 6 [Collections.yaml:12]
- **Schemas:** 84 total, 8 domain-specific, 76 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `CollateralAssetLiquidationProcedure/Created`) [asyncapi:Collections.yaml:9]

## Commission Agreement

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CommissionAgreement.yaml` (sha256 `c0a4f9449f68…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CommissionAgreement.yaml`
- **Purpose (verbatim from spec):** Maintain and administer the terms and transactions for employee and broker commissions [CommissionAgreement.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`broker` in description); Corporate Operations & Support (`employee` in description) [CommissionAgreement.yaml:4]
- **Control Record:** EmployeeCommissionAgreement [CommissionAgreement.yaml:15]
- **Behavior Qualifiers (1):** CommissionTerm [CommissionAgreement.yaml:193]
- **Operations (14):** Control 2, Exchange 2, Grant 2, Initiate 2, Request 2, Retrieve 2, Update 2 [CommissionAgreement.yaml:12]
- **Schemas:** 72 total, 4 domain-specific, 68 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `EmployeeCommissionAgreement/Created`) [asyncapi:CommissionAgreement.yaml:9]
- **Other domains named in this purpose text:** Commissions [CommissionAgreement.yaml:4]

## Commissions

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/Commissions.yaml` (sha256 `9971864a97a1…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: Commissions.yaml`
- **Purpose (verbatim from spec):** The service domain processes commissions for transactions for eligible employees [Commissions.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`service` in description) [Commissions.yaml:4]
- **Control Record:** CommissionTransaction [Commissions.yaml:15]
- **Behavior Qualifiers (3):** Confirmation [Commissions.yaml:167], Calculation [Commissions.yaml:220], Payment [Commissions.yaml:247]
- **Operations (17):** Control 1, Exchange 4, Execute 1, Initiate 2, Request 1, Retrieve 4, Update 4 [Commissions.yaml:12]
- **Schemas:** 131 total, 6 domain-specific, 125 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `CommissionTransaction/Created`) [asyncapi:Commissions.yaml:9]

## Competitor Analysis

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CompetitorAnalysis.yaml` (sha256 `9004856f78c5…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CompetitorAnalysis.yaml`
- **Purpose (verbatim from spec):** Solicit, consolidate and analyze competitor specific public domain data to develop competitor insights and comparisons [CompetitorAnalysis.yaml:4]
- **Theme [derived-rule]:** primary Reference & Data Management; all matches: Reference & Data Management (`data` in description) [CompetitorAnalysis.yaml:4]
- **Control Record:** CompetitorAnalysis [CompetitorAnalysis.yaml:41]
- **Behavior Qualifiers (1):** ProductCompetitiveAnalysis [CompetitorAnalysis.yaml:15]
- **Operations (6):** Evaluate 2, Execute 1, Request 1, Retrieve 2 [CompetitorAnalysis.yaml:12]
- **Schemas:** 40 total, 11 domain-specific, 29 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `CompetitorAnalysis/Created`) [asyncapi:CompetitorAnalysis.yaml:10]

## Compliance Reporting

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ComplianceReporting.yaml` (sha256 `2cb1a328fe19…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: ComplianceReporting.yaml`
- **Purpose (verbatim from spec):** This service domain administers and orchestrates the tasks required to apply and report on internal audit control and reporting activity [ComplianceReporting.yaml:4]
- **Theme [derived-rule]:** primary Risk, Compliance & Fraud; all matches: Risk, Compliance & Fraud (`Complian` in title); Reference & Data Management (`Report` in title); Corporate Operations & Support (`service` in description) [ComplianceReporting.yaml:3]
- **Control Record:** ComplianceReportingAdministrativePlan [ComplianceReporting.yaml:15]
- **Behavior Qualifiers (3):** Consolidation [ComplianceReporting.yaml:65], ComplianceAssessment [ComplianceReporting.yaml:142], Remediation [ComplianceReporting.yaml:195]
- **Operations (18):** Capture 4, Initiate 2, Request 4, Retrieve 4, Update 4 [ComplianceReporting.yaml:12]
- **Schemas:** 64 total, 7 domain-specific, 57 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `ComplianceReportingAdministrativePlan/Created`) [asyncapi:ComplianceReporting.yaml:10]
- **Other domains named in this purpose text:** Internal Audit [ComplianceReporting.yaml:4]

## Consumer Advisory Services

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ConsumerAdvisoryServices.yaml` (sha256 `645283894274…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: ConsumerAdvisoryServices.yaml`
- **Purpose (verbatim from spec):** Offer financial advisory services to consumer customers, possibly for a fee [ConsumerAdvisoryServices.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`Service` in title); Customer, Sales & Marketing (`Offer` in description); Finance, Accounting & Treasury (`financial` in description) [ConsumerAdvisoryServices.yaml:3]
- **Control Record:** ConsumerAdvice [ConsumerAdvisoryServices.yaml:15]
- **Behavior Qualifiers (4):** FinancialPlanning [ConsumerAdvisoryServices.yaml:141], Taxation [ConsumerAdvisoryServices.yaml:219], ProductGuidance [ConsumerAdvisoryServices.yaml:297], Charge [ConsumerAdvisoryServices.yaml:375]
- **Operations (19):** Control 1, Exchange 1, Execute 1, Initiate 5, Request 1, Retrieve 5, Update 5 [ConsumerAdvisoryServices.yaml:12]
- **Schemas:** 114 total, 5 domain-specific, 109 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `ConsumerAdvice/Created`) [asyncapi:ConsumerAdvisoryServices.yaml:9]

## Consumer Investments

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ConsumerInvestments.yaml` (sha256 `e25b33702bb6…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: ConsumerInvestments.yaml`
- **Purpose (verbatim from spec):** Handle the consumer front-end trading requests. These will typically be blocked/netted for market execution [ConsumerInvestments.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Investment` in title) [ConsumerInvestments.yaml:3]
- **Control Record:** ConsumerSecuritiesOrderTransaction [ConsumerInvestments.yaml:40]
- **Behavior Qualifiers (4):** Quote [ConsumerInvestments.yaml:15], Confirmation [ConsumerInvestments.yaml:114], Compliance [ConsumerInvestments.yaml:139], OrderInitiation [ConsumerInvestments.yaml:164]
- **Operations (8):** Exchange 1, Initiate 1, Retrieve 5, Update 1 [ConsumerInvestments.yaml:12]
- **Schemas:** 55 total, 9 domain-specific, 46 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `ConsumerSecuritiesOrderTransaction/Created`) [asyncapi:ConsumerInvestments.yaml:10]

## Consumer Loan

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ConsumerLoan.yaml` (sha256 `39bca23499aa…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: ConsumerLoan.yaml`
- **Purpose (verbatim from spec):** This service domain handles the fulfillment of a consumer loan product. This includes the initial set-up of the loan facility and the completion of scheduled and ad-hoc product processing tasks [ConsumerLoan.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Loan` in title); Customer, Sales & Marketing (`product` in description); Corporate Operations & Support (`service` in description) [ConsumerLoan.yaml:3]
- **Control Record:** ConsumerLoanFacility [ConsumerLoan.yaml:15]
- **Behavior Qualifiers (10):** Interest [ConsumerLoan.yaml:115], Charge [ConsumerLoan.yaml:140], Disbursement [ConsumerLoan.yaml:192], Maintenance [ConsumerLoan.yaml:217], DebitandCredit [ConsumerLoan.yaml:269], Repayment [ConsumerLoan.yaml:375], AmountBlock [ConsumerLoan.yaml:535], IssuedDevice [ConsumerLoan.yaml:613], Booking [ConsumerLoan.yaml:664], Modification [ConsumerLoan.yaml:718]
- **Operations (29):** Control 1, Execute 5, Initiate 3, Request 3, Retrieve 10, Update 7 [ConsumerLoan.yaml:12]
- **Schemas:** 241 total, 39 domain-specific, 202 shared-across-≥10-specs
- **Event channels:** 24 (e.g. `ConsumerLoanFacility/Created`) [asyncapi:ConsumerLoan.yaml:11]

## Contact Center Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ContactCenterManagement.yaml` (sha256 `f67cb61655d2…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: ContactCenterManagement.yaml`
- **Purpose (verbatim from spec):** Oversee the assignment and operation of the customer contact center [ContactCenterManagement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Contact` in title) [ContactCenterManagement.yaml:3]
- **Control Record:** ContactCenterManagementPlan [ContactCenterManagement.yaml:15]
- **Behavior Qualifiers (2):** Performance [ContactCenterManagement.yaml:141], Troubleshooting [ContactCenterManagement.yaml:193]
- **Operations (12):** Create 2, Exchange 1, Request 3, Retrieve 3, Update 3 [ContactCenterManagement.yaml:12]
- **Schemas:** 43 total, 4 domain-specific, 39 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `ContactCenterManagementPlan/Created`) [asyncapi:ContactCenterManagement.yaml:9]

## Contact Center Operations

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ContactCenterOperations.yaml` (sha256 `83ffa4b72beb…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: ContactCenterOperations.yaml`
- **Purpose (verbatim from spec):** Administer the day to day activity in the contact center - allocate positions and track staff availability and performance [ContactCenterOperations.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Contact` in title); Securities, Trading & Markets (`position` in description) [ContactCenterOperations.yaml:3]
- **Control Record:** ContactCenterAdministrativePlan [ContactCenterOperations.yaml:15]
- **Behavior Qualifiers (3):** Assignment [ContactCenterOperations.yaml:167], PeakLoad [ContactCenterOperations.yaml:299], Troubleshooting [ContactCenterOperations.yaml:378]
- **Operations (18):** Control 2, Create 3, Execute 1, Request 4, Retrieve 4, Update 4 [ContactCenterOperations.yaml:12]
- **Schemas:** 39 total, 4 domain-specific, 35 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `ContactCenterAdministrativePlan/Created`) [asyncapi:ContactCenterOperations.yaml:10]

## Contact Handler

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ContactHandler.yaml` (sha256 `1e28636d4f07…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: ContactHandler.yaml`
- **Purpose (verbatim from spec):** This service domain handles a customer's interactive contact with the bank. This will typically involve launching of one or more channel/device specific dialogue sessions as necessary within the customer contact [ContactHandler.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Contact` in title); Channels & Servicing (`channel` in description); Corporate Operations & Support (`service` in description) [ContactHandler.yaml:3]
- **Control Record:** CustomerContactOperatingSession [ContactHandler.yaml:15]
- **Behavior Qualifiers (4):** Authentication [ContactHandler.yaml:193], Routing [ContactHandler.yaml:218], Session [ContactHandler.yaml:243], History [ContactHandler.yaml:375]
- **Operations (16):** Control 2, Exchange 1, Execute 2, Initiate 2, Request 1, Retrieve 5, Update 3 [ContactHandler.yaml:12]
- **Schemas:** 50 total, 10 domain-specific, 40 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `CustomerContactOperatingSession/Created`) [asyncapi:ContactHandler.yaml:11]

## Contact Routing

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ContactRouting.yaml` (sha256 `e900f1b0613d…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: ContactRouting.yaml`
- **Purpose (verbatim from spec):** The Contact Routing service domain tracks servicing resource availability and uses any known details about the customer contact (e.g. identity, indicated purpose of call, status of the relationship) to make an optimal routing decision. The routing selection may include matching the required product… [ContactRouting.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Contact` in title); Channels & Servicing (`servicing` in description); Corporate Operations & Support (`service` in description) [ContactRouting.yaml:3]
- **Control Record:** CustomerServicingResourceAllocation [ContactRouting.yaml:15]
- **Behavior Qualifiers (1):** Allocation [ContactRouting.yaml:167]
- **Operations (12):** Capture 2, Control 2, Exchange 2, Provide 1, Request 1, Retrieve 2, Update 2 [ContactRouting.yaml:12]
- **Schemas:** 39 total, 3 domain-specific, 36 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `CustomerServicingResourceAllocation/Created`) [asyncapi:ContactRouting.yaml:13]

## Contractor and Supplier Agreement

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ContractorandSupplierAgreement.yaml` (sha256 `7ee8115fcddf…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: ContractorandSupplierAgreement.yaml`
- **Purpose (verbatim from spec):** This Service Domain maintains appropriate supplier agreements/contracts [ContractorandSupplierAgreement.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`Contract` in title) [ContractorandSupplierAgreement.yaml:3]
- **Control Record:** SupplierAgreement [ContractorandSupplierAgreement.yaml:15]
- **Behavior Qualifiers (3):** LegalTerm [ContractorandSupplierAgreement.yaml:217], PolicyTerm [ContractorandSupplierAgreement.yaml:270], RegulatoryTerm [ContractorandSupplierAgreement.yaml:296]
- **Operations (26):** Control 1, Evaluate 4, Exchange 4, Grant 1, Notify 4, Request 4, Retrieve 4, Update 4 [ContractorandSupplierAgreement.yaml:12]
- **Schemas:** 85 total, 5 domain-specific, 80 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `SupplierAgreement/Created`) [asyncapi:ContractorandSupplierAgreement.yaml:9]

## Corporate Action

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CorporateAction.yaml` (sha256 `e16a8870666c…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CorporateAction.yaml`
- **Purpose (verbatim from spec):** This Service Domain supports the various custodial tasks associated with processing associated corporate actions for customer's with securities held at the bank [CorporateAction.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`custod` in description); Customer, Sales & Marketing (`customer` in description); Corporate Operations & Support (`Service` in description) [CorporateAction.yaml:4]
- **Control Record:** CorporateActionProcedure [CorporateAction.yaml:15]
- **Behavior Qualifiers (5):** SecurityMergersandAcquisitionAction [CorporateAction.yaml:167], SecurityDividendPayment [CorporateAction.yaml:244], SecurityRightsIssueAction [CorporateAction.yaml:271], SecuritySpin-OffAction [CorporateAction.yaml:298], StockSplitorReversalAction [CorporateAction.yaml:325]
- **Operations (43):** Control 1, Exchange 6, Execute 6, Initiate 6, Notify 6, Request 6, Retrieve 6, Update 6 [CorporateAction.yaml:12]
- **Schemas:** 153 total, 13 domain-specific, 140 shared-across-≥10-specs
- **Event channels:** 20 (e.g. `CorporateActionProcedure/Created`) [asyncapi:CorporateAction.yaml:10]

## Corporate Current Account

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CorporateCurrentAccount.yaml` (sha256 `3320ba515003…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CorporateCurrentAccount.yaml`
- **Purpose (verbatim from spec):** This service domain orchestrates a corporate checking/demand deposit account. The typical range of services and fees covers payments and deposits, standing orders, sweeps, liens, check and debit card access. [CorporateCurrentAccount.yaml:4]
- **Theme [derived-rule]:** primary Deposits & Accounts; all matches: Deposits & Accounts (`Current Account` in title); Payments & Settlement (`payment` in description); Cards & Merchant Services (`card` in description); Finance, Accounting & Treasury (`fees` in description); Corporate Operations & Support (`service` in description) [CorporateCurrentAccount.yaml:3]
- **Control Record:** CorporateCurrentAccountFacility [CorporateCurrentAccount.yaml:15]
- **Behavior Qualifiers (9):** Interest [CorporateCurrentAccount.yaml:115], Charge [CorporateCurrentAccount.yaml:140], Sweep [CorporateCurrentAccount.yaml:218], DebitandCredit [CorporateCurrentAccount.yaml:323], Payment [CorporateCurrentAccount.yaml:428], IssuedDevice [CorporateCurrentAccount.yaml:560], AmountBlock [CorporateCurrentAccount.yaml:692], Deposit [CorporateCurrentAccount.yaml:770], Booking [CorporateCurrentAccount.yaml:822]
- **Operations (34):** Control 1, Exchange 1, Execute 7, Initiate 8, Retrieve 9, Update 8 [CorporateCurrentAccount.yaml:12]
- **Schemas:** 254 total, 40 domain-specific, 214 shared-across-≥10-specs
- **Event channels:** 20 (e.g. `CorporateCurrentAccountFacility/Created`) [asyncapi:CorporateCurrentAccount.yaml:11]

## Corporate Finance

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CorporateFinance.yaml` (sha256 `fa34a83815c3…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CorporateFinance.yaml`
- **Purpose (verbatim from spec):** This Service Domain handles the provision of a broad range of financial advisory services to corporate clients [CorporateFinance.yaml:4]
- **Theme [derived-rule]:** primary Finance, Accounting & Treasury; all matches: Finance, Accounting & Treasury (`financial` in description); Corporate Operations & Support (`Service` in description) [CorporateFinance.yaml:4]
- **Control Record:** CorporateFinanceServicesAdvice [CorporateFinance.yaml:15]
- **Behavior Qualifiers (4):** StrategicFunding [CorporateFinance.yaml:41], Taxation [CorporateFinance.yaml:68], CapitalStructuring [CorporateFinance.yaml:95], TacticalFunding [CorporateFinance.yaml:405]
- **Operations (36):** Control 1, Exchange 5, Execute 5, Initiate 5, Notify 5, Request 5, Retrieve 5, Update 5 [CorporateFinance.yaml:12]
- **Schemas:** 58 total, 9 domain-specific, 49 shared-across-≥10-specs
- **Event channels:** 17 (e.g. `CorporateFinanceServicesAdvice/Created`) [asyncapi:CorporateFinance.yaml:10]

## Corporate Lease

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CorporateLease.yaml` (sha256 `12f41e7ef617…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CorporateLease.yaml`
- **Purpose (verbatim from spec):** The Corporate Lease product provides corporate customers with loans to support leasing activity for property and equipment under an umbrella leasing arrangement [CorporateLease.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`loan` in description); Customer, Sales & Marketing (`product` in description); Corporate Operations & Support (`property` in description) [CorporateLease.yaml:4]
- **Control Record:** CorporateLeaseFacility [CorporateLease.yaml:15]
- **Behavior Qualifiers (2):** Administration [CorporateLease.yaml:193], Fulfill [CorporateLease.yaml:247]
- **Operations (18):** Control 2, Exchange 3, Execute 2, Initiate 2, Request 3, Retrieve 3, Update 3 [CorporateLease.yaml:12]
- **Schemas:** 53 total, 7 domain-specific, 46 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `CorporateLeaseFacility/Created`) [asyncapi:CorporateLease.yaml:10]

## Corporate Loan

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CorporateLoan.yaml` (sha256 `ff1e9a8e5dd5…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CorporateLoan.yaml`
- **Purpose (verbatim from spec):** This service domain handles the fulfillment of a corporate loan product. This includes the initial set-up of the loan facility and the completion of scheduled and ad-hoc product processing tasks [CorporateLoan.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Loan` in title); Customer, Sales & Marketing (`product` in description); Corporate Operations & Support (`service` in description) [CorporateLoan.yaml:3]
- **Control Record:** CorporateLoanFacility [CorporateLoan.yaml:15]
- **Behavior Qualifiers (10):** Interest [CorporateLoan.yaml:115], Charge [CorporateLoan.yaml:140], Disbursement [CorporateLoan.yaml:192], Maintenance [CorporateLoan.yaml:217], DebitandCredit [CorporateLoan.yaml:269], Repayment [CorporateLoan.yaml:375], AmountBlock [CorporateLoan.yaml:535], Booking [CorporateLoan.yaml:613], IssuedDevice [CorporateLoan.yaml:640], Modification [CorporateLoan.yaml:718]
- **Operations (29):** Control 1, Execute 5, Initiate 3, Request 3, Retrieve 10, Update 7 [CorporateLoan.yaml:12]
- **Schemas:** 245 total, 40 domain-specific, 205 shared-across-≥10-specs
- **Event channels:** 24 (e.g. `CorporateLoanFacility/Created`) [asyncapi:CorporateLoan.yaml:11]

## Corporate Payroll Services

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CorporatePayrollServices.yaml` (sha256 `fda2541749f9…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CorporatePayrollServices.yaml`
- **Purpose (verbatim from spec):** The Corporate Payroll Services Service Domain handles payroll payment processing for the employees of a corporate customer. [CorporatePayrollServices.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`Service` in title); Payments & Settlement (`payment` in description); Customer, Sales & Marketing (`customer` in description) [CorporatePayrollServices.yaml:3]
- **Control Record:** EmployeePaymentServicesFacility [CorporatePayrollServices.yaml:15]
- **Behavior Qualifiers (1):** IssueResolution [CorporatePayrollServices.yaml:165]
- **Operations (14):** Control 1, Exchange 1, Execute 2, Initiate 2, Notify 2, Request 2, Retrieve 2, Update 2 [CorporatePayrollServices.yaml:12]
- **Schemas:** 123 total, 4 domain-specific, 119 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `EmployeePaymentServicesFacility/Created`) [asyncapi:CorporatePayrollServices.yaml:10]

## Corporate Tax Advisory

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CorporateTaxAdvisory.yaml` (sha256 `05b65993bf32…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CorporateTaxAdvisory.yaml`
- **Purpose (verbatim from spec):** A fee or commission based product providing tax specific assessments, advice and guidance for corporate customers [CorporateTaxAdvisory.yaml:4]
- **Theme [derived-rule]:** primary Finance, Accounting & Treasury; all matches: Finance, Accounting & Treasury (`Tax` in title); Customer, Sales & Marketing (`product` in description) [CorporateTaxAdvisory.yaml:3]
- **Control Record:** CorporateTaxAdvice [CorporateTaxAdvisory.yaml:15]
- **Behavior Qualifiers (2):** Taxation [CorporateTaxAdvisory.yaml:115], Charge [CorporateTaxAdvisory.yaml:246]
- **Operations (14):** Control 1, Exchange 1, Execute 1, Initiate 3, Request 2, Retrieve 3, Update 3 [CorporateTaxAdvisory.yaml:12]
- **Schemas:** 128 total, 6 domain-specific, 122 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `CorporateTaxAdvice/Created`) [asyncapi:CorporateTaxAdvisory.yaml:10]

## Corporate Treasury

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CorporateTreasury.yaml` (sha256 `f467b9353d2d…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CorporateTreasury.yaml`
- **Purpose (verbatim from spec):** This service domain orchestrates the consolidation and presentation of summary transaction details in order to assemble a timely and accurate view of the overall treasury position of the Bank at any one time. It is also responsible for determining the different interest and exchange rates applied t… [CorporateTreasury.yaml:4]
- **Theme [derived-rule]:** primary Finance, Accounting & Treasury; all matches: Finance, Accounting & Treasury (`Treasury` in title); Securities, Trading & Markets (`position` in description); Reference & Data Management (`rates` in description); Corporate Operations & Support (`service` in description) [CorporateTreasury.yaml:3]
- **Control Record:** CorporateTreasuryManagementPlan [CorporateTreasury.yaml:15]
- **Behavior Qualifiers (5):** Securitization [CorporateTreasury.yaml:91], Liquidity [CorporateTreasury.yaml:118], StrategicFunding [CorporateTreasury.yaml:143], TacticalFunding [CorporateTreasury.yaml:222], BankRates [CorporateTreasury.yaml:272]
- **Operations (11):** Capture 3, Retrieve 6, Update 2 [CorporateTreasury.yaml:12]
- **Schemas:** 50 total, 7 domain-specific, 43 shared-across-≥10-specs
- **Event channels:** 12 (e.g. `CorporateTreasuryManagementPlan/Created`) [asyncapi:CorporateTreasury.yaml:13]

## Corporate Trust Services

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CorporateTrustServices.yaml` (sha256 `a93a5b2cd111…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CorporateTrustServices.yaml`
- **Purpose (verbatim from spec):** This Service Domain provides corporate trust services centered on the handling of debt instruments and escrow account support [CorporateTrustServices.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`Service` in title); Deposits & Accounts (`account` in description) [CorporateTrustServices.yaml:3]
- **Control Record:** CorporateTrustServicesFacility [CorporateTrustServices.yaml:15]
- **Behavior Qualifiers (5):** ProjectFinance [CorporateTrustServices.yaml:217], Escrow [CorporateTrustServices.yaml:271], CourtLiaison [CorporateTrustServices.yaml:298], Financing [CorporateTrustServices.yaml:325], LoanAgencyandAdministration [CorporateTrustServices.yaml:379]
- **Operations (43):** Control 1, Exchange 6, Execute 6, Initiate 6, Notify 6, Request 6, Retrieve 6, Update 6 [CorporateTrustServices.yaml:12]
- **Schemas:** 126 total, 7 domain-specific, 119 shared-across-≥10-specs
- **Event channels:** 20 (e.g. `CorporateTrustServicesFacility/Created`) [asyncapi:CorporateTrustServices.yaml:10]
- **Other domains named in this purpose text:** Trust Services [CorporateTrustServices.yaml:4]

## Correspondence

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/Correspondence.yaml` (sha256 `955b0505dcee…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: Correspondence.yaml`
- **Purpose (verbatim from spec):** This service domain orchestrates the production of pre-formatted correspondence and batches of correspondence (e.g. mail shots). [Correspondence.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Correspondence` in title); Customer, Sales & Marketing (`product` in description); Corporate Operations & Support (`service` in description) [Correspondence.yaml:3]
- **Control Record:** CorrespondenceOperatingSession [Correspondence.yaml:15]
- **Behavior Qualifiers (4):** Outbound [Correspondence.yaml:167], OutboundWithResponse [Correspondence.yaml:192], Inbound [Correspondence.yaml:244], BlockMailing [Correspondence.yaml:271]
- **Operations (18):** Control 1, Execute 1, Initiate 5, Request 1, Retrieve 5, Update 5 [Correspondence.yaml:12]
- **Schemas:** 38 total, 9 domain-specific, 29 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `CorrespondenceOperatingSession/Created`) [asyncapi:Correspondence.yaml:10]

## Correspondent Bank Directory

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CorrespondentBankDirectory.yaml` (sha256 `970b558b67ec…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CorrespondentBankDirectory.yaml`
- **Purpose (verbatim from spec):** This service domain maintains correspondent bank reference details. This includes correspondent bank payment parameters in particular bank limits and capturing transaction activity to track reciprocity [CorrespondentBankDirectory.yaml:4]
- **Theme [derived-rule]:** primary Reference & Data Management; all matches: Reference & Data Management (`Directory` in title); Payments & Settlement (`payment` in description); Corporate Operations & Support (`service` in description) [CorrespondentBankDirectory.yaml:3]
- **Control Record:** CorrespondentBankDirectoryEntry [CorrespondentBankDirectory.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (4):** Register 1, Request 1, Retrieve 1, Update 1 [CorrespondentBankDirectory.yaml:12]
- **Schemas:** 36 total, 4 domain-specific, 32 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `CorrespondentBankDirectoryEntry/Created`) [asyncapi:CorrespondentBankDirectory.yaml:11]

## Correspondent Bank Relationship Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CorrespondentBankRelationshipManagement.yaml` (sha256 `c7dd0701adaf…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CorrespondentBankRelationshipManagement.yaml`
- **Purpose (verbatim from spec):** This Service Domain manages correspondent bank relations, ensuring reciprocity and developing business where possible [CorrespondentBankRelationshipManagement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Relationship` in title); Corporate Operations & Support (`Service` in description) [CorrespondentBankRelationshipManagement.yaml:3]
- **Control Record:** CorrepondentBankRelationshipManagementPlan [CorrespondentBankRelationshipManagement.yaml:15]
- **Behavior Qualifiers (3):** RelationshipReciprocityAssessment [CorrespondentBankRelationshipManagement.yaml:191], IncidentTroubleshootingOversight [CorrespondentBankRelationshipManagement.yaml:218], RelationshipDevelopment [CorrespondentBankRelationshipManagement.yaml:298]
- **Operations (26):** Control 1, Create 1, Exchange 4, Grant 4, Notify 4, Request 4, Retrieve 4, Update 4 [CorrespondentBankRelationshipManagement.yaml:12]
- **Schemas:** 71 total, 8 domain-specific, 63 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `CorrepondentBankRelationshipManagementPlan/Created`) [asyncapi:CorrespondentBankRelationshipManagement.yaml:10]

## Counterparty Administration

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CounterpartyAdministration.yaml` (sha256 `7d6334b4f171…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CounterpartyAdministration.yaml`
- **Purpose (verbatim from spec):** This Service Domain maintains key counterparty reference information used in the clearing and settlement of wholesale trading [CounterpartyAdministration.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`party` in title); Payments & Settlement (`clearing` in description); Securities, Trading & Markets (`trading` in description); Reference & Data Management (`reference` in description); Corporate Operations & Support (`Service` in description) [CounterpartyAdministration.yaml:3]
- **Control Record:** CounterpartyDirectoryEntry [CounterpartyAdministration.yaml:15]
- **Behavior Qualifiers (2):** CounterpartyEntityReference [CounterpartyAdministration.yaml:141], CounterpartyPermittedTransaction [CounterpartyAdministration.yaml:219]
- **Operations (19):** Control 1, Execute 3, Notify 3, Register 3, Request 3, Retrieve 3, Update 3 [CounterpartyAdministration.yaml:12]
- **Schemas:** 60 total, 6 domain-specific, 54 shared-across-≥10-specs
- **Event channels:** 11 (e.g. `CounterpartyDirectoryEntry/Created`) [asyncapi:CounterpartyAdministration.yaml:10]

## Credit Card

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CreditCard.yaml` (sha256 `90acd4e1b213…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CreditCard.yaml`
- **Purpose (verbatim from spec):** This service domain orchestrates the scheduled maintenance and transactional activities associated with credit card product fulfillment [CreditCard.yaml:4]
- **Theme [derived-rule]:** primary Cards & Merchant Services; all matches: Cards & Merchant Services (`Card` in title); Lending & Credit (`Credit` in title); Customer, Sales & Marketing (`product` in description); Corporate Operations & Support (`service` in description) [CreditCard.yaml:3]
- **Control Record:** CreditCardFacility [CreditCard.yaml:15]
- **Behavior Qualifiers (7):** Interest [CreditCard.yaml:63], Charge [CreditCard.yaml:140], Billing [CreditCard.yaml:165], Repayment [CreditCard.yaml:273], CardPayment [CreditCard.yaml:377], IssuedDevice [CreditCard.yaml:456], CreditPlan [CreditCard.yaml:563]
- **Operations (28):** Control 1, Exchange 2, Execute 5, Initiate 3, Request 2, Retrieve 8, Update 7 [CreditCard.yaml:12]
- **Schemas:** 237 total, 28 domain-specific, 209 shared-across-≥10-specs
- **Event channels:** 16 (e.g. `CreditCardFacility/Created`) [asyncapi:CreditCard.yaml:10]

## Credit Facility

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CreditFacility.yaml` (sha256 `6fee7390eb07…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CreditFacility.yaml`
- **Purpose (verbatim from spec):** The Credit Facility Service Domain manages the Credit Facilities that a Corporate Customer has with the bank. A Credit Facility is an agreement between the bank and a (corporate) customer to allow the customer to acquire asset products from the bank up to the limit of the credit facility without th… [CreditFacility.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Credit` in title); Corporate Operations & Support (`Facilit` in title); Cards & Merchant Services (`acquir` in description); Customer, Sales & Marketing (`Customer` in description) [CreditFacility.yaml:3]
- **Control Record:** CreditLineFacility [CreditFacility.yaml:15]
- **Behavior Qualifiers (2):** CreditAllocation [CreditFacility.yaml:39], Charge [CreditFacility.yaml:90]
- **Operations (10):** Execute 1, Initiate 3, Retrieve 3, Update 3 [CreditFacility.yaml:12]
- **Schemas:** 171 total, 14 domain-specific, 157 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `CreditLineFacility/Created`) [asyncapi:CreditFacility.yaml:13]

## Credit Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CreditManagement.yaml` (sha256 `c893d39ea3d2…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CreditManagement.yaml`
- **Purpose (verbatim from spec):** This service domain provides a bank-wide/oversight function to qualify credit pricing for offered products and services to reflect the bank's appetite to write the business. This decision can override the standard product pricing procedure [CreditManagement.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Credit` in title); Customer, Sales & Marketing (`product` in description); Reference & Data Management (`pricing` in description); Corporate Operations & Support (`service` in description) [CreditManagement.yaml:3]
- **Control Record:** CreditPricingAssessment [CreditManagement.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (5):** Evaluate 1, Exchange 1, Grant 1, Retrieve 1, Update 1 [CreditManagement.yaml:12]
- **Schemas:** 41 total, 2 domain-specific, 39 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `CreditPricingAssessment/Created`) [asyncapi:CreditManagement.yaml:11]

## Credit Risk Models

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CreditRiskModels.yaml` (sha256 `0bb0c90f19dc…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CreditRiskModels.yaml`
- **Purpose (verbatim from spec):** This service domain handles the design and maintenance of a portfolio of credit models that are used in all aspects of customer credit assessments [CreditRiskModels.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Credit` in title); Risk, Compliance & Fraud (`Risk` in title); Securities, Trading & Markets (`portfolio` in description); Customer, Sales & Marketing (`customer` in description); Corporate Operations & Support (`service` in description) [CreditRiskModels.yaml:3]
- **Control Record:** CreditRiskModelSpecification [CreditRiskModels.yaml:15]
- **Behavior Qualifiers (3):** FunctionalRequirements [CreditRiskModels.yaml:167], Production [CreditRiskModels.yaml:220], Testing [CreditRiskModels.yaml:272]
- **Operations (19):** Capture 4, Control 1, Exchange 1, Initiate 1, Request 4, Retrieve 4, Update 4 [CreditRiskModels.yaml:12]
- **Schemas:** 28 total, 5 domain-specific, 23 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `CreditRiskModelSpecification/Created`) [asyncapi:CreditRiskModels.yaml:10]

## Credit Risk Operations

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CreditRiskOperations.yaml` (sha256 `eddae329e43c…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CreditRiskOperations.yaml`
- **Purpose (verbatim from spec):** This Service Domain monitors counterparty credit limits in the trading unit [CreditRiskOperations.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Credit` in title); Risk, Compliance & Fraud (`Risk` in title); Securities, Trading & Markets (`trading` in description); Customer, Sales & Marketing (`party` in description); Corporate Operations & Support (`Service` in description) [CreditRiskOperations.yaml:3]
- **Control Record:** TradingCreditPositionMeasurement [CreditRiskOperations.yaml:15]
- **Behavior Qualifiers (1):** TradingCounterpartyCreditLimitIndicator [CreditRiskOperations.yaml:141]
- **Operations (10):** Control 1, Evaluate 2, Execute 2, Notify 2, Request 2, Retrieve 1 [CreditRiskOperations.yaml:12]
- **Schemas:** 90 total, 3 domain-specific, 87 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `TradingCreditPositionMeasurement/Created`) [asyncapi:CreditRiskOperations.yaml:9]

## Currency Exchange

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CurrencyExchange.yaml` (sha256 `5f640871e838…`, version 14.0.0); bundle: `oas3_yamls_part2.md` under `# FILE: CurrencyExchange.yaml`
- **Purpose (verbatim from spec):** Service Domain supports over the counter currency exchange [CurrencyExchange.yaml:4]
- **Theme [derived-rule]:** primary Reference & Data Management; all matches: Reference & Data Management (`Currency` in title); Corporate Operations & Support (`Service` in description) [CurrencyExchange.yaml:3]
- **Control Record:** CurrencyExchangeTransaction [CurrencyExchange.yaml:15]
- **Behavior Qualifiers (3):** FXTransactionCapture [CurrencyExchange.yaml:193], DocumentHandling [CurrencyExchange.yaml:220], Quote [CurrencyExchange.yaml:324]
- **Operations (18):** Control 1, Exchange 2, Execute 2, Initiate 4, Request 1, Retrieve 4, Update 4 [CurrencyExchange.yaml:12]
- **Schemas:** 131 total, 7 domain-specific, 124 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `CurrencyExchangeTransaction/Created`) [asyncapi:CurrencyExchange.yaml:9]

## Current Account

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CurrentAccount.yaml` (sha256 `0e46afcc4b3e…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CurrentAccount.yaml`
- **Purpose (verbatim from spec):** This service domain orchestrates a consumer checking/demand deposit account. The typical range of services and fees covers payments and deposits, standing orders, sweeps, liens, check and debit card access. [CurrentAccount.yaml:4]
- **Theme [derived-rule]:** primary Deposits & Accounts; all matches: Deposits & Accounts (`Current Account` in title); Payments & Settlement (`payment` in description); Cards & Merchant Services (`card` in description); Finance, Accounting & Treasury (`fees` in description); Corporate Operations & Support (`service` in description) [CurrentAccount.yaml:3]
- **Control Record:** CurrentAccountFacility [CurrentAccount.yaml:15]
- **Behavior Qualifiers (9):** Interest [CurrentAccount.yaml:115], Charge [CurrentAccount.yaml:140], Sweep [CurrentAccount.yaml:166], DebitandCredit [CurrentAccount.yaml:323], Payment [CurrentAccount.yaml:428], IssuedDevice [CurrentAccount.yaml:535], Booking [CurrentAccount.yaml:587], Deposit [CurrentAccount.yaml:719], AmountBlock [CurrentAccount.yaml:746]
- **Operations (34):** Control 1, Exchange 1, Execute 7, Initiate 8, Retrieve 9, Update 8 [CurrentAccount.yaml:12]
- **Schemas:** 256 total, 42 domain-specific, 214 shared-across-≥10-specs
- **Event channels:** 20 (e.g. `CurrentAccountFacility/Created`) [asyncapi:CurrentAccount.yaml:11]

## Custody Administration

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustodyAdministration.yaml` (sha256 `8af53f9e076d…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustodyAdministration.yaml`
- **Purpose (verbatim from spec):** A service to provide safe custody services for marketable securities for bank customers [CustodyAdministration.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Custod` in title); Customer, Sales & Marketing (`customer` in description); Corporate Operations & Support (`service` in description) [CustodyAdministration.yaml:3]
- **Control Record:** CustodyFacility [CustodyAdministration.yaml:15]
- **Behavior Qualifiers (5):** Settlement [CustodyAdministration.yaml:89], Dividend [CustodyAdministration.yaml:116], SafeKeeping [CustodyAdministration.yaml:246], Charge [CustodyAdministration.yaml:273], RegulatorySubmission [CustodyAdministration.yaml:326]
- **Operations (26):** Control 2, Exchange 2, Execute 3, Initiate 5, Request 4, Retrieve 6, Update 4 [CustodyAdministration.yaml:12]
- **Schemas:** 57 total, 6 domain-specific, 51 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `CustodyFacility/Created`) [asyncapi:CustodyAdministration.yaml:9]

## Customer Access Entitlement

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerAccessEntitlement.yaml` (sha256 `ce29e41d818e…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerAccessEntitlement.yaml`
- **Purpose (verbatim from spec):** This service domain maintains the details of the allowed channel/device based access to products and services that the customer has in place. This profile is referenced in servicing and fulfillment activity and may include customer preferences and access limits/constraints that span multiple produc… [CustomerAccessEntitlement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title); Channels & Servicing (`channel` in description); Reference & Data Management (`reference` in description); Corporate Operations & Support (`service` in description) [CustomerAccessEntitlement.yaml:3]
- **Control Record:** CustomerAccessProfileAgreement [CustomerAccessEntitlement.yaml:15]
- **Behavior Qualifiers (2):** Restrictions [CustomerAccessEntitlement.yaml:193], Preferences [CustomerAccessEntitlement.yaml:271]
- **Operations (13):** Control 1, Evaluate 3, Exchange 1, Grant 1, Request 1, Retrieve 3, Update 3 [CustomerAccessEntitlement.yaml:12]
- **Schemas:** 40 total, 14 domain-specific, 26 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `CustomerAccessProfileAgreement/Created`) [asyncapi:CustomerAccessEntitlement.yaml:12]

## Customer Agreement

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerAgreement.yaml` (sha256 `b124152e93db…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerAgreement.yaml`
- **Purpose (verbatim from spec):** This service domain maintains the master customer agreement/legal contract. Note that a customer can be a complex corporate entity with many subsidiaries operating in different geopolitical areas. The customer agreement is linked to as many Sales Product Agreements as needed for all in-force produc… [CustomerAgreement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title); Risk, Compliance & Fraud (`legal` in description); Corporate Operations & Support (`service` in description) [CustomerAgreement.yaml:3]
- **Control Record:** CustomerAgreement [CustomerAgreement.yaml:15]
- **Behavior Qualifiers (3):** LegalTerm [CustomerAgreement.yaml:169], RegulatoryTerm [CustomerAgreement.yaml:271], PolicyTerm [CustomerAgreement.yaml:349]
- **Operations (16):** Control 1, Evaluate 4, Exchange 1, Grant 1, Request 1, Retrieve 4, Update 4 [CustomerAgreement.yaml:12]
- **Schemas:** 41 total, 6 domain-specific, 35 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `CustomerAgreement/Created`) [asyncapi:CustomerAgreement.yaml:12]
- **Other domains named in this purpose text:** Sales Product [CustomerAgreement.yaml:4]

## Customer Behavior Insights

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerBehaviorInsights.yaml` (sha256 `bfbdf3bdb041…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerBehaviorInsights.yaml`
- **Purpose (verbatim from spec):** This service domain applies behavioral analysis to customer event history to maintain a range of customer ratings/scores (such as 'propensity to buy') and to detect life events or trends [CustomerBehaviorInsights.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title); Corporate Operations & Support (`service` in description) [CustomerBehaviorInsights.yaml:3]
- **Control Record:** CustomerBehaviorAnalysis [CustomerBehaviorInsights.yaml:15]
- **Behavior Qualifiers (1):** Insight [CustomerBehaviorInsights.yaml:141]
- **Operations (9):** Evaluate 1, Exchange 2, Execute 2, Request 2, Retrieve 2 [CustomerBehaviorInsights.yaml:12]
- **Schemas:** 39 total, 19 domain-specific, 20 shared-across-≥10-specs
- **Event channels:** 16 (e.g. `CustomerBehaviorAnalysis/Created`) [asyncapi:CustomerBehaviorInsights.yaml:11]
- **Other domains named in this purpose text:** Customer Event History [CustomerBehaviorInsights.yaml:4]

## Customer Behavior Models

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerBehaviorModels.yaml` (sha256 `e6b56b41d426…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerBehaviorModels.yaml`
- **Purpose (verbatim from spec):** This service domain handles the design and maintenance of a portfolio of customer behavior models that might be used in all aspects of customer relationship development, sales, servicing and product fulfillment [CustomerBehaviorModels.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title); Securities, Trading & Markets (`portfolio` in description); Channels & Servicing (`servicing` in description); Corporate Operations & Support (`service` in description) [CustomerBehaviorModels.yaml:3]
- **Control Record:** CustomerBehaviorModelSpecification [CustomerBehaviorModels.yaml:15]
- **Behavior Qualifiers (3):** FunctionalRequirements [CustomerBehaviorModels.yaml:115], Testing [CustomerBehaviorModels.yaml:248], Production [CustomerBehaviorModels.yaml:327]
- **Operations (15):** Capture 1, Create 1, Exchange 2, Execute 2, Request 3, Retrieve 4, Update 2 [CustomerBehaviorModels.yaml:12]
- **Schemas:** 40 total, 12 domain-specific, 28 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `CustomerBehaviorModelSpecification/Created`) [asyncapi:CustomerBehaviorModels.yaml:11]

## Customer Billing

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerBilling.yaml` (sha256 `c2cf8c294820…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerBilling.yaml`
- **Purpose (verbatim from spec):** This service domains provides a central service to compose, issue and track customer billing and invoices [CustomerBilling.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title); Finance, Accounting & Treasury (`Billing` in title); Channels & Servicing (`voice` in description); Corporate Operations & Support (`service` in description) [CustomerBilling.yaml:3]
- **Control Record:** CustomerBillingProcedure [CustomerBilling.yaml:15]
- **Behavior Qualifiers (3):** Invoicing [CustomerBilling.yaml:167], TrackingandReminders [CustomerBilling.yaml:219], Payment [CustomerBilling.yaml:272]
- **Operations (15):** Control 1, Exchange 2, Execute 1, Initiate 3, Request 1, Retrieve 4, Update 3 [CustomerBilling.yaml:12]
- **Schemas:** 101 total, 10 domain-specific, 91 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `CustomerBillingProcedure/Created`) [asyncapi:CustomerBilling.yaml:10]

## Customer Campaign Design

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerCampaignDesign.yaml` (sha256 `f75d0de5a986…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerCampaignDesign.yaml`
- **Purpose (verbatim from spec):** Design and refine customer campaign specifications based on their impact [CustomerCampaignDesign.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title) [CustomerCampaignDesign.yaml:3]
- **Control Record:** CustomerCampaignSpecification [CustomerCampaignDesign.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (8):** Capture 1, Control 1, Create 1, Exchange 1, Execute 1, Request 1, Retrieve 1, Update 1 [CustomerCampaignDesign.yaml:12]
- **Schemas:** 66 total, 25 domain-specific, 41 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `CustomerCampaignSpecification/Created`) [asyncapi:CustomerCampaignDesign.yaml:9]

## Customer Campaign Execution

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerCampaignExecution.yaml` (sha256 `d330c182161b…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerCampaignExecution.yaml`
- **Purpose (verbatim from spec):** Execute a customer campaign (version) and track and respond to impact [CustomerCampaignExecution.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title) [CustomerCampaignExecution.yaml:3]
- **Control Record:** CustomerCampaignProcedure [CustomerCampaignExecution.yaml:15]
- **Behavior Qualifiers (3):** CandidateSelection [CustomerCampaignExecution.yaml:193], Execution [CustomerCampaignExecution.yaml:272], AnalysisFeedback [CustomerCampaignExecution.yaml:377]
- **Operations (18):** Control 1, Exchange 2, Execute 1, Initiate 3, Request 3, Retrieve 4, Update 4 [CustomerCampaignExecution.yaml:12]
- **Schemas:** 75 total, 16 domain-specific, 59 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `CustomerCampaignProcedure/Created`) [asyncapi:CustomerCampaignExecution.yaml:9]

## Customer Campaign Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerCampaignManagement.yaml` (sha256 `d3f21d714dcd…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerCampaignManagement.yaml`
- **Purpose (verbatim from spec):** Assess the coverage and impact of internal/customer campaigns and redirect campaign development and execution activity accordingly [CustomerCampaignManagement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title) [CustomerCampaignManagement.yaml:3]
- **Control Record:** CustomerCampaignPortfolioManagementPlan [CustomerCampaignManagement.yaml:15]
- **Behavior Qualifiers (3):** MarketTracking [CustomerCampaignManagement.yaml:117], PerformanceAssessment [CustomerCampaignManagement.yaml:247], CampaignDirection [CustomerCampaignManagement.yaml:379]
- **Operations (18):** Create 3, Execute 2, Grant 1, Request 4, Retrieve 4, Update 4 [CustomerCampaignManagement.yaml:12]
- **Schemas:** 99 total, 26 domain-specific, 73 shared-across-≥10-specs
- **Event channels:** 16 (e.g. `CustomerCampaignPortfolioManagementPlan/Created`) [asyncapi:CustomerCampaignManagement.yaml:10]

## Customer Case

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerCase.yaml` (sha256 `40a52a85ccf4…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerCase.yaml`
- **Purpose (verbatim from spec):** This service domain handles the initiation, tracking, resolution and reporting on customer cases (issues that typically require corrective response to some financial transaction) [CustomerCase.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title); Channels & Servicing (`Case` in title); Finance, Accounting & Treasury (`financial` in description); Reference & Data Management (`report` in description); Corporate Operations & Support (`service` in description) [CustomerCase.yaml:3]
- **Control Record:** CustomerCaseProcedure [CustomerCase.yaml:15]
- **Behavior Qualifiers (3):** Analysis [CustomerCase.yaml:193], Determination [CustomerCase.yaml:245], Resolution [CustomerCase.yaml:297]
- **Operations (14):** Control 1, Exchange 2, Execute 1, Initiate 1, Request 1, Retrieve 4, Update 4 [CustomerCase.yaml:12]
- **Schemas:** 81 total, 8 domain-specific, 73 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `CustomerCaseProcedure/Created`) [asyncapi:CustomerCase.yaml:10]

## Customer Case Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerCaseManagement.yaml` (sha256 `a1c5e37b539b…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerCaseManagement.yaml`
- **Purpose (verbatim from spec):** Track and assess case load and resolution activity - allocate resources as necessary to optimize case resolution performance [CustomerCaseManagement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title); Channels & Servicing (`Case` in title) [CustomerCaseManagement.yaml:3]
- **Control Record:** CustomerCaseManagementPlan [CustomerCaseManagement.yaml:15]
- **Behavior Qualifiers (2):** Rules [CustomerCaseManagement.yaml:141], Performance [CustomerCaseManagement.yaml:220]
- **Operations (11):** Create 1, Exchange 1, Request 3, Retrieve 3, Update 3 [CustomerCaseManagement.yaml:12]
- **Schemas:** 44 total, 3 domain-specific, 41 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `CustomerCaseManagementPlan/Created`) [asyncapi:CustomerCaseManagement.yaml:10]

## Customer Credit Rating

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerCreditRating.yaml` (sha256 `c5f21538b233…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerCreditRating.yaml`
- **Purpose (verbatim from spec):** This service domain maintains and administers the bank's credit assessment for customers based on consolidated internal data and optionally by referencing external credit agency reports [CustomerCreditRating.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Credit` in title); Customer, Sales & Marketing (`Customer` in title); Reference & Data Management (`data` in description); Corporate Operations & Support (`service` in description) [CustomerCreditRating.yaml:3]
- **Control Record:** CustomerCreditRatingState [CustomerCreditRating.yaml:15]
- **Behavior Qualifiers (3):** Alerts [CustomerCreditRating.yaml:167], InternalReporting [CustomerCreditRating.yaml:219], ExternalReporting [CustomerCreditRating.yaml:271]
- **Operations (12):** Capture 3, Control 1, Exchange 1, Execute 1, Initiate 1, Request 1, Retrieve 4 [CustomerCreditRating.yaml:12]
- **Schemas:** 45 total, 10 domain-specific, 35 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `CustomerCreditRatingState/Created`) [asyncapi:CustomerCreditRating.yaml:11]

## Customer Event History

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerEventHistory.yaml` (sha256 `d422a485b4c7…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerEventHistory.yaml`
- **Purpose (verbatim from spec):** This service domain captures, classifies and stores relationship, servicing and product fulfillment related customer events. In addition to servicing and product transaction details, the log can capture life/relationship events that are revealed during customer exchanges [CustomerEventHistory.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title); Channels & Servicing (`servicing` in description); Corporate Operations & Support (`service` in description) [CustomerEventHistory.yaml:3]
- **Control Record:** CustomerEventLog [CustomerEventHistory.yaml:42]
- **Behavior Qualifiers (6):** Relationship [CustomerEventHistory.yaml:15], Sales [CustomerEventHistory.yaml:194], Servicing [CustomerEventHistory.yaml:273], ProductProcessing [CustomerEventHistory.yaml:352], Fraud [CustomerEventHistory.yaml:431], Life [CustomerEventHistory.yaml:510]
- **Operations (22):** Capture 6, Control 1, Initiate 1, Retrieve 7, Update 7 [CustomerEventHistory.yaml:12]
- **Schemas:** 58 total, 13 domain-specific, 45 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `CustomerEventLog/Created`) [asyncapi:CustomerEventHistory.yaml:12]

## Customer Financial Insights

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerFinancialInsights.yaml` (sha256 `70805f72dc17…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerFinancialInsights.yaml`
- **Purpose (verbatim from spec):** This service domain applies behavioral analysis to the customer financial history to develop financial insights that can highlight business development opportunities or detect possible concerns with a customer's financial wellfare [CustomerFinancialInsights.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title); Finance, Accounting & Treasury (`Financial` in title); Corporate Operations & Support (`service` in description) [CustomerFinancialInsights.yaml:3]
- **Control Record:** CustomerFinancialPositionAnalysis [CustomerFinancialInsights.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (1):** Retrieve 1 [CustomerFinancialInsights.yaml:12]
- **Schemas:** 40 total, 15 domain-specific, 25 shared-across-≥10-specs
- **Event channels:** 22 (e.g. `CustomerFinancialPositionAnalysis/Created`) [asyncapi:CustomerFinancialInsights.yaml:11]
- **Other domains named in this purpose text:** Business Development [CustomerFinancialInsights.yaml:4]

## Customer Offer

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerOffer.yaml` (sha256 `d7efcd587d9d…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerOffer.yaml`
- **Purpose (verbatim from spec):** This service domain orchestrates the processing of a product offer for a new or established customer. The offer process is defined specifically for the product or service being considered and can include actions such as document checks, collateral allocation, credit assessments, underwriting decisi… [CustomerOffer.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title); Lending & Credit (`collateral` in description); Securities, Trading & Markets (`underwrit` in description); Corporate Operations & Support (`service` in description) [CustomerOffer.yaml:3]
- **Control Record:** CustomerOfferProcedure [CustomerOffer.yaml:15]
- **Behavior Qualifiers (11):** FacilityApplication [CustomerOffer.yaml:67], Disclosures [CustomerOffer.yaml:248], Underwriting [CustomerOffer.yaml:326], Credit [CustomerOffer.yaml:403], Compliance [CustomerOffer.yaml:455], Audit [CustomerOffer.yaml:507], CollateralAllocation [CustomerOffer.yaml:534], Booking [CustomerOffer.yaml:638], CorrespondenceandDocuments [CustomerOffer.yaml:690], Agreement [CustomerOffer.yaml:769], ProductInitialization [CustomerOffer.yaml:848]
- **Operations (34):** Control 1, Exchange 6, Execute 1, Initiate 1, Request 1, Retrieve 12, Update 12 [CustomerOffer.yaml:12]
- **Schemas:** 181 total, 33 domain-specific, 148 shared-across-≥10-specs
- **Event channels:** 24 (e.g. `CustomerOfferProcedure/Created`) [asyncapi:CustomerOffer.yaml:14]
- **Other domains named in this purpose text:** Underwriting [CustomerOffer.yaml:4]

## Customer Portfolio

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerPortfolio.yaml` (sha256 `dc822c5be99c…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerPortfolio.yaml`
- **Purpose (verbatim from spec):** Maintain a portfolio of analytical views of the customer base to support customer segment profitability and performance analysis [CustomerPortfolio.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Portfolio` in title); Customer, Sales & Marketing (`Customer` in title); Reference & Data Management (`analytic` in description) [CustomerPortfolio.yaml:3]
- **Control Record:** CustomerPortfolioAnalysis [CustomerPortfolio.yaml:15]
- **Behavior Qualifiers (1):** PerformanceAnalysis [CustomerPortfolio.yaml:115]
- **Operations (10):** Evaluate 2, Exchange 1, Execute 1, Request 2, Retrieve 2, Update 2 [CustomerPortfolio.yaml:12]
- **Schemas:** 63 total, 11 domain-specific, 52 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `CustomerPortfolioAnalysis/Created`) [asyncapi:CustomerPortfolio.yaml:10]

## Customer Position

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerPosition.yaml` (sha256 `5f225181d5f6…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerPosition.yaml`
- **Purpose (verbatim from spec):** This service domain maintains a consolidated financial position for a customer, combining details from all products and services in use. The position can cover available funds, credit, collateral, tax exposure and other financial measures as necessary [CustomerPosition.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Position` in title); Customer, Sales & Marketing (`Customer` in title); Lending & Credit (`credit` in description); Finance, Accounting & Treasury (`financial` in description); Corporate Operations & Support (`service` in description) [CustomerPosition.yaml:3]
- **Control Record:** CustomerPositionState [CustomerPosition.yaml:15]
- **Behavior Qualifiers (3):** Cashflow [CustomerPosition.yaml:167], Credit [CustomerPosition.yaml:246], CollateralAllocation [CustomerPosition.yaml:325]
- **Operations (19):** Capture 3, Control 1, Evaluate 2, Exchange 3, Execute 1, Initiate 1, Notify 2, Request 1, Retrieve 4, Update 1 [CustomerPosition.yaml:12]
- **Schemas:** 82 total, 15 domain-specific, 67 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `CustomerPositionState/Created`) [asyncapi:CustomerPosition.yaml:12]

## Customer Product And Service Eligibility

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerProductAndServiceEligibility.yaml` (sha256 `f7da89ddd79a…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerProductAndServiceEligibility.yaml`
- **Purpose (verbatim from spec):** This Service Domain maintains a list of products and services for which a customer is eligible. [CustomerProductAndServiceEligibility.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title); Corporate Operations & Support (`Service` in title) [CustomerProductAndServiceEligibility.yaml:3]
- **Control Record:** CustomerEligibilityAssessment [CustomerProductAndServiceEligibility.yaml:15]
- **Behavior Qualifiers (2):** EligibilityCheck [CustomerProductAndServiceEligibility.yaml:193], NextBest [CustomerProductAndServiceEligibility.yaml:218]
- **Operations (11):** Evaluate 2, Exchange 1, Execute 1, Grant 1, Request 1, Retrieve 3, Update 2 [CustomerProductAndServiceEligibility.yaml:12]
- **Schemas:** 56 total, 9 domain-specific, 47 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `CustomerEligibilityAssessment/Created`) [asyncapi:CustomerProductAndServiceEligibility.yaml:9]

## Customer Product and Service Directory

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerProductandServiceDirectory.yaml` (sha256 `e01209e3b987…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerProductandServiceDirectory.yaml`
- **Purpose (verbatim from spec):** This Service Domain maintains the most important details of all the products and services that a customer has acquired from the bank. [CustomerProductandServiceDirectory.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title); Reference & Data Management (`Directory` in title); Corporate Operations & Support (`Service` in title); Cards & Merchant Services (`acquir` in description) [CustomerProductandServiceDirectory.yaml:3]
- **Control Record:** CustomerProductAndServiceDirectoryEntry [CustomerProductandServiceDirectory.yaml:15]
- **Behavior Qualifiers (2):** Product [CustomerProductandServiceDirectory.yaml:191], Service [CustomerProductandServiceDirectory.yaml:218]
- **Operations (19):** Control 1, Execute 3, Notify 3, Register 3, Request 3, Retrieve 3, Update 3 [CustomerProductandServiceDirectory.yaml:12]
- **Schemas:** 37 total, 6 domain-specific, 31 shared-across-≥10-specs
- **Event channels:** 11 (e.g. `CustomerProductAndServiceDirectoryEntry/Created`) [asyncapi:CustomerProductandServiceDirectory.yaml:10]

## Customer Proposition

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerProposition.yaml` (sha256 `4a7e25a39b60…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerProposition.yaml`
- **Purpose (verbatim from spec):** This Service Domain maintains bank and customer defined requirements spanning all products and services [CustomerProposition.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title); Corporate Operations & Support (`Service` in description) [CustomerProposition.yaml:3]
- **Control Record:** CustomerPropositionAgreement [CustomerProposition.yaml:15]
- **Behavior Qualifiers (2):** BankDefinedProductandServiceTerm [CustomerProposition.yaml:217], CustomerDefinedProductandServiceTerm [CustomerProposition.yaml:243]
- **Operations (21):** Control 1, Evaluate 3, Exchange 3, Execute 1, Grant 1, Notify 3, Request 3, Retrieve 3, Update 3 [CustomerProposition.yaml:12]
- **Schemas:** 84 total, 4 domain-specific, 80 shared-across-≥10-specs
- **Event channels:** 11 (e.g. `CustomerPropositionAgreement/Created`) [asyncapi:CustomerProposition.yaml:10]

## Customer Relationship Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerRelationshipManagement.yaml` (sha256 `f57a0da7053e…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerRelationshipManagement.yaml`
- **Purpose (verbatim from spec):** This service domain develops and executes a customer plan to maintain and build a customer relationship. Activities include ongoing customer contact, tracking internal and external events and activity of interest and relevance, product and service matching and sales, processing ad-hoc queries, trou… [CustomerRelationshipManagement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title); Corporate Operations & Support (`service` in description) [CustomerRelationshipManagement.yaml:3]
- **Control Record:** CustomerRelationshipManagementPlan [CustomerRelationshipManagement.yaml:15]
- **Behavior Qualifiers (3):** Development [CustomerRelationshipManagement.yaml:193], Incident [CustomerRelationshipManagement.yaml:325], Contact [CustomerRelationshipManagement.yaml:484]
- **Operations (22):** Capture 1, Control 2, Create 4, Exchange 3, Grant 1, Request 3, Retrieve 4, Update 4 [CustomerRelationshipManagement.yaml:12]
- **Schemas:** 71 total, 18 domain-specific, 53 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `CustomerRelationshipManagementPlan/Created`) [asyncapi:CustomerRelationshipManagement.yaml:13]

## Customer Surveys

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerSurveys.yaml` (sha256 `8f04af072b4a…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerSurveys.yaml`
- **Purpose (verbatim from spec):** Define and execute and analyze customer surveys [CustomerSurveys.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title) [CustomerSurveys.yaml:3]
- **Behavior Qualifiers:** none
- **Operations:** none defined (the OpenAPI `paths` section is empty or absent)
- **Schemas:** 6 total, 5 domain-specific, 1 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `CustomerSurveyProcedure/Created`) [asyncapi:CustomerSurveys.yaml:9]

## Customer Tax Handling

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerTaxHandling.yaml` (sha256 `05ee3e89266e…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerTaxHandling.yaml`
- **Purpose (verbatim from spec):** This service domain handles consumer tax reporting obligations including the consolidation and reporting of customer tax related financial activity [CustomerTaxHandling.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title); Finance, Accounting & Treasury (`Tax` in title); Reference & Data Management (`report` in description); Corporate Operations & Support (`service` in description) [CustomerTaxHandling.yaml:3]
- **Control Record:** CustomerTaxObligationFacility [CustomerTaxHandling.yaml:15]
- **Behavior Qualifiers (3):** Consolidation [CustomerTaxHandling.yaml:167], Analysis [CustomerTaxHandling.yaml:219], Reporting [CustomerTaxHandling.yaml:298]
- **Operations (14):** Control 1, Exchange 2, Execute 1, Initiate 1, Request 1, Retrieve 4, Update 4 [CustomerTaxHandling.yaml:12]
- **Schemas:** 134 total, 4 domain-specific, 130 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `CustomerTaxObligationFacility/Created`) [asyncapi:CustomerTaxHandling.yaml:10]

## Customer Workbench

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/CustomerWorkbench.yaml` (sha256 `e491dfd95f6f…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: CustomerWorkbench.yaml`
- **Purpose (verbatim from spec):** This service domain represents customer side devices. Most commonly providing a customer access portal to the banks products and services through any suitable channel and device [CustomerWorkbench.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Customer` in title); Channels & Servicing (`channel` in description); Corporate Operations & Support (`service` in description) [CustomerWorkbench.yaml:3]
- **Control Record:** CustomerWorkbenchOperatingSession [CustomerWorkbench.yaml:15]
- **Behavior Qualifiers (5):** SWUpdate [CustomerWorkbench.yaml:39], Broadcast [CustomerWorkbench.yaml:166], Browsing [CustomerWorkbench.yaml:192], Contact [CustomerWorkbench.yaml:218], ProductandServiceAccess [CustomerWorkbench.yaml:456]
- **Operations (23):** Control 1, Evaluate 1, Exchange 1, Execute 3, Initiate 6, Request 3, Retrieve 5, Update 3 [CustomerWorkbench.yaml:12]
- **Schemas:** 25 total, 6 domain-specific, 19 shared-across-≥10-specs
- **Event channels:** 12 (e.g. `CustomerWorkbenchOperatingSession/Created`) [asyncapi:CustomerWorkbench.yaml:11]

## Dealer Desk

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/DealerDesk.yaml` (sha256 `cddccbbabd62…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: DealerDesk.yaml`
- **Purpose (verbatim from spec):** The Dealer Workbench represents the bank's dealing desk facility supporting one or more trading lines of activity for both agency and principal trading in all chosen market instruments. It also supports sales and market risk trading desk functions [DealerDesk.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`trading` in description); Risk, Compliance & Fraud (`risk` in description); Customer, Sales & Marketing (`sales` in description); Corporate Operations & Support (`facilit` in description) [DealerDesk.yaml:4]
- **Control Record:** DealerDeskOperatingSession [DealerDesk.yaml:15]
- **Behavior Qualifiers (3):** DealerDeskConsolidatedPositionTracking [DealerDesk.yaml:217], DealerDeskTradingAssignmentandLimits [DealerDesk.yaml:244], InformationFeedAdministration [DealerDesk.yaml:271]
- **Operations (29):** Control 1, Exchange 4, Execute 4, Initiate 4, Notify 4, Request 4, Retrieve 4, Update 4 [DealerDesk.yaml:12]
- **Schemas:** 35 total, 5 domain-specific, 30 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `DealerDeskOperatingSession/Created`) [asyncapi:DealerDesk.yaml:11]

## Delinquent Account Handling

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/DelinquentAccountHandling.yaml` (sha256 `9456c0eeb6bd…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: DelinquentAccountHandling.yaml`
- **Purpose (verbatim from spec):** This service domain handles delinquent accounts (typically for active credit/charge cards) for follow-up of payments due through periodic review and contacts. This process ends when the account is cancelled and is transferred to Collections [DelinquentAccountHandling.yaml:4]
- **Theme [derived-rule]:** primary Deposits & Accounts; all matches: Deposits & Accounts (`Account` in title); Payments & Settlement (`payment` in description); Cards & Merchant Services (`cards` in description); Lending & Credit (`credit` in description); Customer, Sales & Marketing (`contact` in description); Corporate Operations & Support (`service` in description) [DelinquentAccountHandling.yaml:3]
- **Control Record:** DelinquentAccountProcedure [DelinquentAccountHandling.yaml:15]
- **Behavior Qualifiers (4):** Assessment [DelinquentAccountHandling.yaml:65], Contact [DelinquentAccountHandling.yaml:90], Payment [DelinquentAccountHandling.yaml:116], Resolution [DelinquentAccountHandling.yaml:349]
- **Operations (16):** Control 1, Exchange 2, Execute 1, Initiate 3, Request 1, Retrieve 5, Update 3 [DelinquentAccountHandling.yaml:12]
- **Schemas:** 144 total, 5 domain-specific, 139 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `DelinquentAccountProcedure/Created`) [asyncapi:DelinquentAccountHandling.yaml:11]
- **Other domains named in this purpose text:** Collections [DelinquentAccountHandling.yaml:4]

## Direct Debit

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/DirectDebit.yaml` (sha256 `bb044b8ec84b…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: DirectDebit.yaml`
- **Purpose (verbatim from spec):** Fulfils a direct debit agreement. Handles the creditor side of direct debits. [DirectDebit.yaml:4]
- **Theme [derived-rule]:** primary Payments & Settlement; all matches: Payments & Settlement (`Direct Debit` in title); Lending & Credit (`credit` in description) [DirectDebit.yaml:3]
- **Control Record:** DirectDebitFacility [DirectDebit.yaml:15]
- **Behavior Qualifiers (2):** PaymentBatch [DirectDebit.yaml:41], Reporting [DirectDebit.yaml:66]
- **Operations (11):** Control 1, Exchange 1, Execute 2, Initiate 2, Request 1, Retrieve 3, Update 1 [DirectDebit.yaml:12]
- **Schemas:** 76 total, 4 domain-specific, 72 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `DirectDebitFacility/Created`) [asyncapi:DirectDebit.yaml:9]

## Direct Debit Mandate

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/DirectDebitMandate.yaml` (sha256 `27233ae58209…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: DirectDebitMandate.yaml`
- **Purpose (verbatim from spec):** This service domains manages the customer mandates associated with direct debit processing for a corporate client [DirectDebitMandate.yaml:4]
- **Theme [derived-rule]:** primary Payments & Settlement; all matches: Payments & Settlement (`Direct Debit` in title); Customer, Sales & Marketing (`customer` in description); Corporate Operations & Support (`service` in description) [DirectDebitMandate.yaml:3]
- **Control Record:** DirectDebitMandateDirectoryEntry [DirectDebitMandate.yaml:15]
- **Behavior Qualifiers (1):** MandateRegistration [DirectDebitMandate.yaml:115]
- **Operations (10):** Control 1, Exchange 1, Execute 1, Register 2, Request 1, Retrieve 2, Update 2 [DirectDebitMandate.yaml:12]
- **Schemas:** 124 total, 8 domain-specific, 116 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `DirectDebitMandateDirectoryEntry/Created`) [asyncapi:DirectDebitMandate.yaml:10]
- **Other domains named in this purpose text:** Direct Debit [DirectDebitMandate.yaml:4]

## Disbursement

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/Disbursement.yaml` (sha256 `84b503fbb159…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: Disbursement.yaml`
- **Purpose (verbatim from spec):** This service domain handles the disbursement of funds to newly established loans/facilities as necessary [Disbursement.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`loan` in description); Securities, Trading & Markets (`funds` in description); Corporate Operations & Support (`service` in description) [Disbursement.yaml:4]
- **Control Record:** DisbursementTransaction [Disbursement.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (7):** Control 1, Exchange 1, Execute 1, Initiate 1, Request 1, Retrieve 1, Update 1 [Disbursement.yaml:12]
- **Schemas:** 109 total, 4 domain-specific, 105 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `DisbursementTransaction/Created`) [asyncapi:Disbursement.yaml:9]

## Document Directory

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/DocumentDirectory.yaml` (sha256 `6f42d3a9df0e…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: DocumentDirectory.yaml`
- **Purpose (verbatim from spec):** This Service Domain provides a directory based categorization and storage mechanism for documents created and referenced by the bank [DocumentDirectory.yaml:4]
- **Theme [derived-rule]:** primary Reference & Data Management; all matches: Reference & Data Management (`Directory` in title); Corporate Operations & Support (`Document` in title) [DocumentDirectory.yaml:3]
- **Control Record:** DocumentDirectoryEntry [DocumentDirectory.yaml:15]
- **Behavior Qualifiers (6):** DocumentAmendmentProperties [DocumentDirectory.yaml:217], DocumentArchivingProperties [DocumentDirectory.yaml:244], DocumentReferenceProperties [DocumentDirectory.yaml:271], DocumentUpdateHistoryProperties [DocumentDirectory.yaml:298], DocumentVerificationProperties [DocumentDirectory.yaml:325], DocumentVersionProperties [DocumentDirectory.yaml:352]
- **Operations (44):** Control 1, Exchange 1, Execute 7, Notify 7, Register 7, Request 7, Retrieve 7, Update 7 [DocumentDirectory.yaml:12]
- **Schemas:** 73 total, 12 domain-specific, 61 shared-across-≥10-specs
- **Event channels:** 23 (e.g. `DocumentDirectoryEntry/Created`) [asyncapi:DocumentDirectory.yaml:10]

## Document Services

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/DocumentServices.yaml` (sha256 `895118b952f8…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: DocumentServices.yaml`
- **Purpose (verbatim from spec):** The Document Services Service Domain manages the creation and maintenance of documents throughout the bank. [DocumentServices.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`Document` in title) [DocumentServices.yaml:3]
- **Control Record:** DocumentServiceProcedure [DocumentServices.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (6):** Control 1, Exchange 1, Execute 1, Initiate 1, Notify 1, Request 1 [DocumentServices.yaml:12]
- **Schemas:** 82 total, 7 domain-specific, 75 shared-across-≥10-specs
- **Event channels:** 5 (e.g. `DocumentServiceProcedure/Created`) [asyncapi:DocumentServices.yaml:10]

## ECM And DCM

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ECMAndDCM.yaml` (sha256 `a44a521f6b4a…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: ECMAndDCM.yaml`
- **Purpose (verbatim from spec):** Supports the specification, pricing and issuance of equity and debt (bond) primary capital market products for corporate financing services [ECMAndDCM.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`bond` in description); Customer, Sales & Marketing (`product` in description); Finance, Accounting & Treasury (`capital` in description); Reference & Data Management (`pricing` in description); Corporate Operations & Support (`service` in description) [ECMAndDCM.yaml:4]
- **Control Record:** ECMAndDCMFacility [ECMAndDCM.yaml:15]
- **Behavior Qualifiers (3):** InstrumentDesign [ECMAndDCM.yaml:39], Prospectus [ECMAndDCM.yaml:196], Placement [ECMAndDCM.yaml:250]
- **Operations (14):** Exchange 1, Initiate 1, Request 4, Retrieve 4, Update 4 [ECMAndDCM.yaml:12]
- **Schemas:** 62 total, 6 domain-specific, 56 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `ECMAndDCMFacility/Created`) [asyncapi:ECMAndDCM.yaml:10]

## Enterprise Architecture

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/EnterpriseArchitecture.yaml` (sha256 `b39702bb9498…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: EnterpriseArchitecture.yaml`
- **Purpose (verbatim from spec):** Define and maintain comprehensive business architectural definitions/blueprints to help organize/direct the business [EnterpriseArchitecture.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`Enterprise` in title) [EnterpriseArchitecture.yaml:3]
- **Control Record:** EnterpriseArchitectureSpecification [EnterpriseArchitecture.yaml:15]
- **Behavior Qualifiers (5):** TechnologyInfrastructure [EnterpriseArchitecture.yaml:141], BusinessArchitecture [EnterpriseArchitecture.yaml:194], ApplicationArchitecture [EnterpriseArchitecture.yaml:221], Organization [EnterpriseArchitecture.yaml:248], InformationArchitecture [EnterpriseArchitecture.yaml:301]
- **Operations (27):** Capture 6, Control 1, Exchange 1, Initiate 1, Request 6, Retrieve 6, Update 6 [EnterpriseArchitecture.yaml:12]
- **Schemas:** 30 total, 7 domain-specific, 23 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `EnterpriseArchitectureSpecification/Created`) [asyncapi:EnterpriseArchitecture.yaml:10]

## Factoring

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/Factoring.yaml` (sha256 `ae743b35e760…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: Factoring.yaml`
- **Purpose (verbatim from spec):** This Service Domain supports a factoring service for corporate customers enabling them to convert accounts receivable into immediate funds at a discount [Factoring.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Factoring` in title); Securities, Trading & Markets (`funds` in description); Deposits & Accounts (`account` in description); Customer, Sales & Marketing (`customer` in description); Finance, Accounting & Treasury (`receivable` in description); Corporate Operations & Support (`Service` in description) [Factoring.yaml:3]
- **Control Record:** FactoringFacility [Factoring.yaml:15]
- **Behavior Qualifiers (4):** AccountReceivableFactoring [Factoring.yaml:217], FactoringProcessing [Factoring.yaml:244], FactoringEvaluation [Factoring.yaml:271], FactoringPurchase [Factoring.yaml:298]
- **Operations (36):** Control 1, Exchange 5, Execute 5, Initiate 5, Notify 5, Request 5, Retrieve 5, Update 5 [Factoring.yaml:12]
- **Schemas:** 125 total, 6 domain-specific, 119 shared-across-≥10-specs
- **Event channels:** 17 (e.g. `FactoringFacility/Created`) [asyncapi:Factoring.yaml:10]
- **Other domains named in this purpose text:** Accounts Receivable [Factoring.yaml:4]

## Fiduciary Agreement

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/FiduciaryAgreement.yaml` (sha256 `ef34d4ef60b4…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: FiduciaryAgreement.yaml`
- **Purpose (verbatim from spec):** An agreement where the bank agrees to act on behalf of the customer in a financial matter and in accordance with the agreement terms [FiduciaryAgreement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`customer` in description); Finance, Accounting & Treasury (`financial` in description) [FiduciaryAgreement.yaml:4]
- **Behavior Qualifiers (2):** Fiduciary [FiduciaryAgreement.yaml:15], Charge [FiduciaryAgreement.yaml:42]
- **Operations (8):** Exchange 2, Initiate 1, Request 2, Retrieve 2, Update 1 [FiduciaryAgreement.yaml:12]
- **Schemas:** 81 total, 2 domain-specific, 79 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `FiduciaryRelationshipAgreement/Created`) [asyncapi:FiduciaryAgreement.yaml:10]

## Financial Accounting

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/FinancialAccounting.yaml` (sha256 `dd6a2b294288…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: FinancialAccounting.yaml`
- **Purpose (verbatim from spec):** The Financial Accounting Service Domain takes in financial facts and based on these, creates accounting instructions that will update the general ledger and sub ledger accounts [FinancialAccounting.yaml:4]
- **Theme [derived-rule]:** primary Deposits & Accounts; all matches: Deposits & Accounts (`Account` in title); Finance, Accounting & Treasury (`Financial` in title); Corporate Operations & Support (`Service` in description) [FinancialAccounting.yaml:3]
- **Control Record:** FinancialBookingLog [FinancialAccounting.yaml:15]
- **Behavior Qualifiers (1):** LedgerPosting [FinancialAccounting.yaml:115]
- **Operations (7):** Capture 1, Control 1, Initiate 1, Retrieve 2, Update 2 [FinancialAccounting.yaml:12]
- **Schemas:** 39 total, 2 domain-specific, 37 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `FinancialBookingLog/Created`) [asyncapi:FinancialAccounting.yaml:11]

## Financial Gateway

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/FinancialGateway.yaml` (sha256 `ec1a419c0182…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: FinancialGateway.yaml`
- **Purpose (verbatim from spec):** This service domain operates automated message interfaces to secure networks such as SWIFT, TELEX, ACH and Financial Market/Exchange reporting services [FinancialGateway.yaml:4]
- **Theme [derived-rule]:** primary Finance, Accounting & Treasury; all matches: Finance, Accounting & Treasury (`Financial` in title); Payments & Settlement (`ACH` in description); Securities, Trading & Markets (`Market` in description); Reference & Data Management (`report` in description); Corporate Operations & Support (`service` in description) [FinancialGateway.yaml:3]
- **Control Record:** FinancialGatewayOperatingSession [FinancialGateway.yaml:15]
- **Behavior Qualifiers (2):** Inbound [FinancialGateway.yaml:141], Outbound [FinancialGateway.yaml:192]
- **Operations (9):** Control 1, Initiate 3, Request 1, Retrieve 3, Update 1 [FinancialGateway.yaml:12]
- **Schemas:** 28 total, 7 domain-specific, 21 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `FinancialGatewayOperatingSession/Created`) [asyncapi:FinancialGateway.yaml:10]

## Financial Instrument Reference Data Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/FinancialInstrumentReferenceDataManagement.yaml` (sha256 `35ee746fefac…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: FinancialInstrumentReferenceDataManagement.yaml`
- **Purpose (verbatim from spec):** This Service Domain maintains a directory of financial instrument reference data [FinancialInstrumentReferenceDataManagement.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Financial Instrument` in title); Finance, Accounting & Treasury (`Financial` in title); Reference & Data Management (`Reference` in title); Corporate Operations & Support (`Service` in description) [FinancialInstrumentReferenceDataManagement.yaml:3]
- **Control Record:** FinancialInstrumentDirectoryEntry [FinancialInstrumentReferenceDataManagement.yaml:15]
- **Behavior Qualifiers (6):** DebtInstrument [FinancialInstrumentReferenceDataManagement.yaml:191], Equity [FinancialInstrumentReferenceDataManagement.yaml:218], Futures [FinancialInstrumentReferenceDataManagement.yaml:245], Option [FinancialInstrumentReferenceDataManagement.yaml:272], Warrant [FinancialInstrumentReferenceDataManagement.yaml:299], Currency [FinancialInstrumentReferenceDataManagement.yaml:949]
- **Operations (40):** Control 1, Execute 6, Notify 6, Register 7, Request 6, Retrieve 7, Update 7 [FinancialInstrumentReferenceDataManagement.yaml:12]
- **Schemas:** 50 total, 13 domain-specific, 37 shared-across-≥10-specs
- **Event channels:** 22 (e.g. `FinancialInstrumentDirectoryEntry/Created`) [asyncapi:FinancialInstrumentReferenceDataManagement.yaml:9]

## Financial Instrument Valuation

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/FinancialInstrumentValuation.yaml` (sha256 `8d6db2909cc5…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: FinancialInstrumentValuation.yaml`
- **Purpose (verbatim from spec):** This Service Domain provides a range of financial asset valuation services [FinancialInstrumentValuation.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Financial Instrument` in title); Finance, Accounting & Treasury (`Financial` in title); Corporate Operations & Support (`Service` in description) [FinancialInstrumentValuation.yaml:3]
- **Control Record:** MarketAssetValuationProcedure [FinancialInstrumentValuation.yaml:15]
- **Behavior Qualifiers (3):** AssetValuationApproachSelection [FinancialInstrumentValuation.yaml:217], AssetValuationInformationConsolidation [FinancialInstrumentValuation.yaml:244], AssetValuation [FinancialInstrumentValuation.yaml:298]
- **Operations (29):** Control 1, Exchange 4, Execute 4, Initiate 4, Notify 4, Request 4, Retrieve 4, Update 4 [FinancialInstrumentValuation.yaml:12]
- **Schemas:** 76 total, 5 domain-specific, 71 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `MarketAssetValuationProcedure/Created`) [asyncapi:FinancialInstrumentValuation.yaml:9]

## Financial Market Analysis

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/FinancialMarketAnalysis.yaml` (sha256 `1219be19c162…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: FinancialMarketAnalysis.yaml`
- **Purpose (verbatim from spec):** Provide different types of financial market analysis using available financial market information and research [FinancialMarketAnalysis.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Market` in title); Finance, Accounting & Treasury (`Financial` in title); Reference & Data Management (`information` in description) [FinancialMarketAnalysis.yaml:3]
- **Control Record:** FinancialMarketAnalysis [FinancialMarketAnalysis.yaml:15]
- **Behavior Qualifiers (1):** FinancialMarketInsight [FinancialMarketAnalysis.yaml:141]
- **Operations (10):** Execute 2, Initiate 2, Request 2, Retrieve 2, Update 2 [FinancialMarketAnalysis.yaml:12]
- **Schemas:** 29 total, 3 domain-specific, 26 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `FinancialMarketAnalysis/Created`) [asyncapi:FinancialMarketAnalysis.yaml:10]
- **Other domains named in this purpose text:** Market Analysis [FinancialMarketAnalysis.yaml:4]

## Financial Market Research

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/FinancialMarketResearch.yaml` (sha256 `4ed43c79637f…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: FinancialMarketResearch.yaml`
- **Purpose (verbatim from spec):** The service domain consolidates external financial market research [FinancialMarketResearch.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Market` in title); Finance, Accounting & Treasury (`Financial` in title); Corporate Operations & Support (`service` in description) [FinancialMarketResearch.yaml:3]
- **Control Record:** FinancialMarketResearchDirectoryEntry [FinancialMarketResearch.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (5):** Execute 1, Register 1, Request 1, Retrieve 1, Update 1 [FinancialMarketResearch.yaml:12]
- **Schemas:** 31 total, 5 domain-specific, 26 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `FinancialMarketResearchDirectoryEntry/Created`) [asyncapi:FinancialMarketResearch.yaml:9]
- **Other domains named in this purpose text:** Market Research [FinancialMarketResearch.yaml:4]

## Financial Statement Assessment

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/FinancialStatementAssessment.yaml` (sha256 `9610e61ab5ca…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: FinancialStatementAssessment.yaml`
- **Purpose (verbatim from spec):** This Service Domain supports a range of financial analyses that can be used to extract specific insights (e.g. valuations, liquidity, risk, market sensitivities) from an entity's financial statements [FinancialStatementAssessment.yaml:4]
- **Theme [derived-rule]:** primary Finance, Accounting & Treasury; all matches: Finance, Accounting & Treasury (`Financial` in title); Securities, Trading & Markets (`market` in description); Risk, Compliance & Fraud (`risk` in description); Corporate Operations & Support (`Service` in description) [FinancialStatementAssessment.yaml:3]
- **Control Record:** FinancialStatementAssessment [FinancialStatementAssessment.yaml:15]
- **Behavior Qualifiers (4):** AssetandLiabilityValuationTest [FinancialStatementAssessment.yaml:165], LiquidityandCashFlowTest [FinancialStatementAssessment.yaml:191], RiskTest [FinancialStatementAssessment.yaml:217], SensitivityTest [FinancialStatementAssessment.yaml:243]
- **Operations (26):** Evaluate 5, Execute 5, Grant 1, Notify 5, Request 5, Retrieve 5 [FinancialStatementAssessment.yaml:12]
- **Schemas:** 45 total, 6 domain-specific, 39 shared-across-≥10-specs
- **Event channels:** 17 (e.g. `FinancialStatementAssessment/Created`) [asyncapi:FinancialStatementAssessment.yaml:11]

## Fraud Diagnosis

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/FraudDiagnosis.yaml` (sha256 `489ab51d8c5d…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: FraudDiagnosis.yaml`
- **Purpose (verbatim from spec):** This service domain handles the evaluation of detected possible fraud to support an appropriate response to contain the exposure [FraudDiagnosis.yaml:4]
- **Theme [derived-rule]:** primary Risk, Compliance & Fraud; all matches: Risk, Compliance & Fraud (`Fraud` in title); Corporate Operations & Support (`service` in description) [FraudDiagnosis.yaml:3]
- **Control Record:** FraudDiagnosisAnalysis [FraudDiagnosis.yaml:15]
- **Behavior Qualifiers (3):** EconomicModel [FraudDiagnosis.yaml:117], CustomerBehavior [FraudDiagnosis.yaml:166], AnalystReview [FraudDiagnosis.yaml:191]
- **Operations (9):** Evaluate 1, Exchange 1, Request 2, Retrieve 4, Update 1 [FraudDiagnosis.yaml:12]
- **Schemas:** 33 total, 6 domain-specific, 27 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `FraudDiagnosisAnalysis/Created`) [asyncapi:FraudDiagnosis.yaml:10]

## Fraud Evaluation

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/FraudEvaluation.yaml` (sha256 `e95e7a21fc7a…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: FraudEvaluation.yaml`
- **Purpose (verbatim from spec):** The service domain executes fraud behavioral pattern tests to detect possible fraudulent transactions/activity [FraudEvaluation.yaml:4]
- **Theme [derived-rule]:** primary Risk, Compliance & Fraud; all matches: Risk, Compliance & Fraud (`Fraud` in title); Corporate Operations & Support (`service` in description) [FraudEvaluation.yaml:3]
- **Control Record:** FraudEvaluationAssessment [FraudEvaluation.yaml:15]
- **Behavior Qualifiers (2):** RuleSetsandDecisionTrees [FraudEvaluation.yaml:91], Models [FraudEvaluation.yaml:192]
- **Operations (8):** Evaluate 1, Exchange 1, Execute 1, Grant 1, Request 1, Retrieve 3 [FraudEvaluation.yaml:12]
- **Schemas:** 27 total, 4 domain-specific, 23 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `FraudEvaluationAssessment/Created`) [asyncapi:FraudEvaluation.yaml:10]

## Fraud Model

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/FraudModel.yaml` (sha256 `dd1737a3ff11…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: FraudModel.yaml`
- **Purpose (verbatim from spec):** This service domain handles the design and maintenance of a portfolio of fraud models used across all production activity to detect potential fraud on the part of customers, merchants and other involved parties [FraudModel.yaml:4]
- **Theme [derived-rule]:** primary Risk, Compliance & Fraud; all matches: Risk, Compliance & Fraud (`Fraud` in title); Reference & Data Management (`Model` in title); Cards & Merchant Services (`merchant` in description); Securities, Trading & Markets (`portfolio` in description); Customer, Sales & Marketing (`product` in description); Corporate Operations & Support (`service` in description) [FraudModel.yaml:3]
- **Control Record:** FraudModelSpecification [FraudModel.yaml:15]
- **Behavior Qualifiers (3):** FunctionalRequirements [FraudModel.yaml:115], Testing [FraudModel.yaml:248], Production [FraudModel.yaml:327]
- **Operations (15):** Capture 1, Create 1, Exchange 2, Execute 2, Request 3, Retrieve 4, Update 2 [FraudModel.yaml:12]
- **Schemas:** 50 total, 7 domain-specific, 43 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `FraudModelSpecification/Created`) [asyncapi:FraudModel.yaml:11]

## Fraud Resolution

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/FraudResolution.yaml` (sha256 `570d48092142…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: FraudResolution.yaml`
- **Purpose (verbatim from spec):** This service domain sets up and processes a fraud case resulting from fraud behavior that has been detected during production processing [FraudResolution.yaml:4]
- **Theme [derived-rule]:** primary Risk, Compliance & Fraud; all matches: Risk, Compliance & Fraud (`Fraud` in title); Customer, Sales & Marketing (`product` in description); Channels & Servicing (`case` in description); Corporate Operations & Support (`service` in description) [FraudResolution.yaml:3]
- **Control Record:** FraudResolutionProcedure [FraudResolution.yaml:15]
- **Behavior Qualifiers (3):** CaseAnalysis [FraudResolution.yaml:91], CaseDetermination [FraudResolution.yaml:140], CaseResolution [FraudResolution.yaml:192]
- **Operations (9):** Exchange 2, Initiate 1, Request 1, Retrieve 4, Update 1 [FraudResolution.yaml:12]
- **Schemas:** 162 total, 18 domain-specific, 144 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `FraudResolutionProcedure/Created`) [asyncapi:FraudResolution.yaml:10]

## Funeral Policy

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/FuneralPolicy.yaml` (sha256 `db27822ffd6b…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: FuneralPolicy.yaml`
- **Purpose (verbatim from spec):** The Funeral Policy Service Domain handles the general product maintenance, premium payments and initiates claims processing. [FuneralPolicy.yaml:4]
- **Theme [derived-rule]:** primary Risk, Compliance & Fraud; all matches: Risk, Compliance & Fraud (`Polic` in title); Payments & Settlement (`payment` in description); Customer, Sales & Marketing (`product` in description); Corporate Operations & Support (`Service` in description) [FuneralPolicy.yaml:3]
- **Behavior Qualifiers:** none
- **Operations:** none defined (the OpenAPI `paths` section is empty or absent)
- **Schemas:** 6 total, 4 domain-specific, 2 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `FuneralPolicyFacility/Created`) [asyncapi:FuneralPolicy.yaml:10]

## Guideline Compliance

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/GuidelineCompliance.yaml` (sha256 `e62794088da9…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: GuidelineCompliance.yaml`
- **Purpose (verbatim from spec):** This service domain develops and applies a portfolio of guideline compliance tests to confirm adherence to bank and regulator imposed internal procedures. Tests may be made on complete transaction data or a meaningful samples as appropriate to mitigate exposure to non-compliant behaviors. Complianc… [GuidelineCompliance.yaml:4]
- **Theme [derived-rule]:** primary Risk, Compliance & Fraud; all matches: Risk, Compliance & Fraud (`Complian` in title); Securities, Trading & Markets (`portfolio` in description); Reference & Data Management (`data` in description); Corporate Operations & Support (`service` in description) [GuidelineCompliance.yaml:3]
- **Control Record:** GuidelineComplianceAssessment [GuidelineCompliance.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (5):** Evaluate 1, Exchange 1, Request 1, Retrieve 1, Update 1 [GuidelineCompliance.yaml:12]
- **Schemas:** 43 total, 1 domain-specific, 42 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `GuidelineComplianceAssessment/Created`) [asyncapi:GuidelineCompliance.yaml:14]

## Hedge Fund Administration

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/HedgeFundAdministration.yaml` (sha256 `1ae842ae1232…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: HedgeFundAdministration.yaml`
- **Purpose (verbatim from spec):** The Hedge Fund Administration Service Domain handles all aspects of the set-up and operation of a hedge fund that is offered to accredited investors within the bank's customer base [HedgeFundAdministration.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Fund` in title); Lending & Credit (`credit` in description); Customer, Sales & Marketing (`customer` in description); Corporate Operations & Support (`Service` in description) [HedgeFundAdministration.yaml:3]
- **Control Record:** HedgeFundAdministrativePlan [HedgeFundAdministration.yaml:15]
- **Behavior Qualifiers (9):** FundAccounting [HedgeFundAdministration.yaml:193], FundEnrolmentCertification [HedgeFundAdministration.yaml:220], FundDevelopment [HedgeFundAdministration.yaml:271], FundInvestor_MiddleandBackOfficeService [HedgeFundAdministration.yaml:298], FundInflowsandOutflow [HedgeFundAdministration.yaml:352], FundFinancialReporting [HedgeFundAdministration.yaml:379], FundManagement [HedgeFundAdministration.yaml:433], FundPerformanceFee [HedgeFundAdministration.yaml:460], FundTaxAdministration [HedgeFundAdministration.yaml:487]
- **Operations (62):** Control 1, Create 1, Exchange 10, Grant 10, Notify 10, Request 10, Retrieve 10, Update 10 [HedgeFundAdministration.yaml:12]
- **Schemas:** 74 total, 12 domain-specific, 62 shared-across-≥10-specs
- **Event channels:** 32 (e.g. `HedgeFundAdministrativePlan/Created`) [asyncapi:HedgeFundAdministration.yaml:11]

## IT Standards And Guidelines

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ITStandardsAndGuidelines.yaml` (sha256 `23fa8872b4ed…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: ITStandardsAndGuidelines.yaml`
- **Purpose (verbatim from spec):** Define and apply comprehensive IT architectures, policies and standards as appropriate. Also define the IT usage guidelines and procedures governing systems use across the enterprise [ITStandardsAndGuidelines.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`IT` in title); Risk, Compliance & Fraud (`polic` in description) [ITStandardsAndGuidelines.yaml:3]
- **Control Record:** TechnologyStandardsSpecification [ITStandardsAndGuidelines.yaml:15]
- **Behavior Qualifiers (5):** DevelopmentToolingandEnvironment [ITStandardsAndGuidelines.yaml:193], ITPoliciesandGuidelines [ITStandardsAndGuidelines.yaml:220], ProductTestingandDeploymentMechanisms [ITStandardsAndGuidelines.yaml:273], ProductionPlatformsandInfrastructure [ITStandardsAndGuidelines.yaml:300], ProductionEnvironmentandSupportServices [ITStandardsAndGuidelines.yaml:407]
- **Operations (37):** Capture 6, Control 1, Exchange 6, Initiate 6, Request 6, Retrieve 6, Update 6 [ITStandardsAndGuidelines.yaml:12]
- **Schemas:** 30 total, 7 domain-specific, 23 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `TechnologyStandardsSpecification/Created`) [asyncapi:ITStandardsAndGuidelines.yaml:11]

## Incentive Account

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/IncentiveAccount.yaml` (sha256 `7231fb412f61…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: IncentiveAccount.yaml`
- **Purpose (verbatim from spec):** This service domain orchestrates the scheduled maintenance and transactional activities associated with Incentive Program fulfillment, including enrollment, accrual and redemption. [IncentiveAccount.yaml:4]
- **Theme [derived-rule]:** primary Deposits & Accounts; all matches: Deposits & Accounts (`Account` in title); Corporate Operations & Support (`service` in description) [IncentiveAccount.yaml:3]
- **Behavior Qualifiers:** none
- **Operations:** none defined (the OpenAPI `paths` section is empty or absent)
- **Schemas:** 2 total, 1 domain-specific, 1 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `IncentiveAccountFacility/Created`) [asyncapi:IncentiveAccount.yaml:11]

## Incentive Program Directory

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/IncentiveProgramDirectory.yaml` (sha256 `18187a22b751…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: IncentiveProgramDirectory.yaml`
- **Purpose (verbatim from spec):** This service domain maintains specifications of the various Incentive Programs that are on offerr to customers. [IncentiveProgramDirectory.yaml:4]
- **Theme [derived-rule]:** primary Reference & Data Management; all matches: Reference & Data Management (`Directory` in title); Customer, Sales & Marketing (`customer` in description); Corporate Operations & Support (`service` in description) [IncentiveProgramDirectory.yaml:3]
- **Behavior Qualifiers:** none
- **Operations:** none defined (the OpenAPI `paths` section is empty or absent)
- **Schemas:** 2 total, 1 domain-specific, 1 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `IncentiveProgramDirectoryEntry/Created`) [asyncapi:IncentiveProgramDirectory.yaml:10]

## Information Provider Operation

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/InformationProviderOperation.yaml` (sha256 `4d1e3f29e674…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: InformationProviderOperation.yaml`
- **Purpose (verbatim from spec):** none given [InformationProviderOperation.yaml:3]
- **Theme [derived-rule]:** primary Reference & Data Management; all matches: Reference & Data Management (`Information` in title) [InformationProviderOperation.yaml:3]
- **Control Record:** InformationFeedOperatingSession [InformationProviderOperation.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (8):** Control 1, Exchange 1, Execute 1, Initiate 1, Notify 1, Request 1, Retrieve 1, Update 1 [InformationProviderOperation.yaml:12]
- **Schemas:** 24 total, 2 domain-specific, 22 shared-across-≥10-specs
- **Event channels:** 5 (e.g. `InformationFeedOperatingSession/Created`) [asyncapi:InformationProviderOperation.yaml:7]

## Intellectual Property Portfolio

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/IntellectualPropertyPortfolio.yaml` (sha256 `dc37c3d6b16d…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: IntellectualPropertyPortfolio.yaml`
- **Purpose (verbatim from spec):** Administer the bank's intellectual property assets [IntellectualPropertyPortfolio.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Portfolio` in title); Corporate Operations & Support (`Property` in title) [IntellectualPropertyPortfolio.yaml:3]
- **Control Record:** IntellectualPropertyAdministrativePlan [IntellectualPropertyPortfolio.yaml:15]
- **Behavior Qualifiers (2):** Maintenance [IntellectualPropertyPortfolio.yaml:89], Assignment [IntellectualPropertyPortfolio.yaml:194]
- **Operations (14):** Exchange 2, Grant 1, Initiate 3, Request 2, Retrieve 3, Update 3 [IntellectualPropertyPortfolio.yaml:12]
- **Schemas:** 52 total, 4 domain-specific, 48 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `IntellectualPropertyAdministrativePlan/Created`) [asyncapi:IntellectualPropertyPortfolio.yaml:9]

## Interactive Help

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/InteractiveHelp.yaml` (sha256 `3e6bad9802ce…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: InteractiveHelp.yaml`
- **Purpose (verbatim from spec):** Operate the automated facility that provides interactive context sensitive servicing guidance to employees and self-serve customers [InteractiveHelp.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`customer` in description); Channels & Servicing (`servicing` in description); Corporate Operations & Support (`facilit` in description) [InteractiveHelp.yaml:4]
- **Behavior Qualifiers (1):** HelpServiceSelection [InteractiveHelp.yaml:15]
- **Operations (4):** Capture 1, Execute 1, Initiate 1, Retrieve 1 [InteractiveHelp.yaml:12]
- **Schemas:** 9 total, 3 domain-specific, 6 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `HelpServiceSelection/Created`) [asyncapi:InteractiveHelp.yaml:10]

## Interbank Relationship Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/InterbankRelationshipManagement.yaml` (sha256 `eb3e539e757d…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: InterbankRelationshipManagement.yaml`
- **Purpose (verbatim from spec):** Manage the bank's relationship with other banks, covering any specific agreements that may be in place and overseeing operational issues. [InterbankRelationshipManagement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Relationship` in title) [InterbankRelationshipManagement.yaml:3]
- **Control Record:** BankRelationshipManagementPlan [InterbankRelationshipManagement.yaml:15]
- **Behavior Qualifiers (1):** Contact [InterbankRelationshipManagement.yaml:193]
- **Operations (11):** Control 1, Create 2, Exchange 1, Grant 1, Request 2, Retrieve 2, Update 2 [InterbankRelationshipManagement.yaml:12]
- **Schemas:** 44 total, 5 domain-specific, 39 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `BankRelationshipManagementPlan/Created`) [asyncapi:InterbankRelationshipManagement.yaml:10]

## Internal Audit

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/InternalAudit.yaml` (sha256 `d78d58a7724e…`, version 14.0.0); bundle: `oas3_yamls_part3.md` under `# FILE: InternalAudit.yaml`
- **Purpose (verbatim from spec):** Maintain and portfolio of internal audit checks. Select and execute a meaningful sample of checks and identify and resolve non-compliance [InternalAudit.yaml:4]
- **Theme [derived-rule]:** primary Risk, Compliance & Fraud; all matches: Risk, Compliance & Fraud (`Audit` in title); Securities, Trading & Markets (`portfolio` in description) [InternalAudit.yaml:3]
- **Control Record:** InternalAuditAssessment [InternalAudit.yaml:15]
- **Behavior Qualifiers (1):** Audit [InternalAudit.yaml:193]
- **Operations (14):** Exchange 2, Execute 2, Grant 2, Initiate 2, Request 2, Retrieve 2, Update 2 [InternalAudit.yaml:12]
- **Schemas:** 41 total, 3 domain-specific, 38 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `InternalAuditAssessment/Created`) [asyncapi:InternalAudit.yaml:10]

## Internal Bank Account

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/InternalBankAccount.yaml` (sha256 `ba713af312e9…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: InternalBankAccount.yaml`
- **Purpose (verbatim from spec):** This Service Domain manages the banking-related accounts that are not owned by customers. These are not general ledger accounts. Typical examples are holding accounts and mirror accounts. [InternalBankAccount.yaml:4]
- **Theme [derived-rule]:** primary Deposits & Accounts; all matches: Deposits & Accounts (`Account` in title); Customer, Sales & Marketing (`customer` in description); Finance, Accounting & Treasury (`ledger` in description); Corporate Operations & Support (`Service` in description) [InternalBankAccount.yaml:3]
- **Control Record:** InternalBankAccountFacility [InternalBankAccount.yaml:15]
- **Behavior Qualifiers (1):** Booking [InternalBankAccount.yaml:91]
- **Operations (7):** Capture 1, Control 1, Execute 1, Initiate 1, Notify 1, Retrieve 1, Update 1 [InternalBankAccount.yaml:12]
- **Schemas:** 135 total, 20 domain-specific, 115 shared-across-≥10-specs
- **Event channels:** 5 (e.g. `InternalBankAccountFacility/Created`) [asyncapi:InternalBankAccount.yaml:11]

## Investment Account

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/InvestmentAccount.yaml` (sha256 `e9eaf186d73a…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: InvestmentAccount.yaml`
- **Purpose (verbatim from spec):** This service domain handles the non-cash holdings positions for a customer, covering multiple instruments as necessary [InvestmentAccount.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Investment` in title); Deposits & Accounts (`Account` in title); Customer, Sales & Marketing (`customer` in description); Finance, Accounting & Treasury (`cash` in description); Corporate Operations & Support (`service` in description) [InvestmentAccount.yaml:3]
- **Control Record:** InvestmentAccountFacility [InvestmentAccount.yaml:15]
- **Behavior Qualifiers (4):** DebitandCredit [InvestmentAccount.yaml:91], CorporateAction [InvestmentAccount.yaml:116], Charge [InvestmentAccount.yaml:325], Deposit [InvestmentAccount.yaml:511]
- **Operations (25):** Control 1, Exchange 4, Execute 4, Initiate 5, Request 1, Retrieve 5, Update 5 [InvestmentAccount.yaml:12]
- **Schemas:** 132 total, 15 domain-specific, 117 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `InvestmentAccountFacility/Created`) [asyncapi:InvestmentAccount.yaml:10]

## Investment Portfolio Analysis

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/InvestmentPortfolioAnalysis.yaml` (sha256 `4f69bb925237…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: InvestmentPortfolioAnalysis.yaml`
- **Purpose (verbatim from spec):** Assess and report on investment portfolio make-up, valuation and performance [InvestmentPortfolioAnalysis.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Investment` in title); Reference & Data Management (`report` in description) [InvestmentPortfolioAnalysis.yaml:3]
- **Control Record:** ManagedInvestmentPortfolioAnalysis [InvestmentPortfolioAnalysis.yaml:15]
- **Behavior Qualifiers (1):** PerformanceAnalysis [InvestmentPortfolioAnalysis.yaml:141]
- **Operations (9):** Evaluate 1, Exchange 2, Execute 2, Request 2, Retrieve 2 [InvestmentPortfolioAnalysis.yaml:12]
- **Schemas:** 35 total, 5 domain-specific, 30 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `ManagedInvestmentPortfolioAnalysis/Created`) [asyncapi:InvestmentPortfolioAnalysis.yaml:9]

## Investment Portfolio Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/InvestmentPortfolioManagement.yaml` (sha256 `6ee855d9f64a…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: InvestmentPortfolioManagement.yaml`
- **Purpose (verbatim from spec):** Manage an investment portfolio, initiating trading to leverage market opportunities, remaining within portfolio trading policies [InvestmentPortfolioManagement.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Investment` in title); Risk, Compliance & Fraud (`polic` in description) [InvestmentPortfolioManagement.yaml:3]
- **Control Record:** ManagedInvestmentPortfolioFacility [InvestmentPortfolioManagement.yaml:15]
- **Behavior Qualifiers (3):** Opportunity [InvestmentPortfolioManagement.yaml:169], FinancialStatusTracking [InvestmentPortfolioManagement.yaml:218], Trade [InvestmentPortfolioManagement.yaml:243]
- **Operations (14):** Control 1, Exchange 2, Execute 1, Initiate 2, Request 2, Retrieve 4, Update 2 [InvestmentPortfolioManagement.yaml:12]
- **Schemas:** 26 total, 6 domain-specific, 20 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `ManagedInvestmentPortfolioFacility/Created`) [asyncapi:InvestmentPortfolioManagement.yaml:10]

## Investment Portfolio Planning

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/InvestmentPortfolioPlanning.yaml` (sha256 `68a10485d75f…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: InvestmentPortfolioPlanning.yaml`
- **Purpose (verbatim from spec):** Agree the policies and required make-up of an investment portfolio and ensure all required bank and regulatory terms and conditions are addressed [InvestmentPortfolioPlanning.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Investment` in title); Risk, Compliance & Fraud (`polic` in description) [InvestmentPortfolioPlanning.yaml:3]
- **Control Record:** ManagedInvestmentPortfolioAgreement [InvestmentPortfolioPlanning.yaml:15]
- **Behavior Qualifiers (1):** InvestmentTerms [InvestmentPortfolioPlanning.yaml:141]
- **Operations (11):** Control 1, Evaluate 2, Exchange 1, Grant 1, Request 2, Retrieve 2, Update 2 [InvestmentPortfolioPlanning.yaml:12]
- **Schemas:** 36 total, 2 domain-specific, 34 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `ManagedInvestmentPortfolioAgreement/Created`) [asyncapi:InvestmentPortfolioPlanning.yaml:10]

## Issued Certificate Directory

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/IssuedCertificateDirectory.yaml` (sha256 `824afa90c2ca…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: IssuedCertificateDirectory.yaml`
- **Purpose (verbatim from spec):** This service domain faciliatates the issuance of Rewards Certificates and their redemption. [IssuedCertificateDirectory.yaml:4]
- **Theme [derived-rule]:** primary Reference & Data Management; all matches: Reference & Data Management (`Directory` in title); Corporate Operations & Support (`service` in description) [IssuedCertificateDirectory.yaml:3]
- **Behavior Qualifiers:** none
- **Operations:** none defined (the OpenAPI `paths` section is empty or absent)
- **Schemas:** 2 total, 1 domain-specific, 1 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `IssuedCertificateDirectoryEntry/Created`) [asyncapi:IssuedCertificateDirectory.yaml:9]

## Issued Device Administration

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/IssuedDeviceAdministration.yaml` (sha256 `9c457d2cafd8…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: IssuedDeviceAdministration.yaml`
- **Purpose (verbatim from spec):** This service domain administers the issuance of authentication tokens to customers and third party service providers. Tokens here include physical devices such as cards, fobs, readers and intangible 'devices' such as passwords and secret questions. Administration includes version tracking, replacem… [IssuedDeviceAdministration.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`Device` in title); Cards & Merchant Services (`cards` in description); Customer, Sales & Marketing (`customer` in description) [IssuedDeviceAdministration.yaml:3]
- **Control Record:** IssuedDeviceAllocation [IssuedDeviceAdministration.yaml:15]
- **Behavior Qualifiers (7):** PasswordAssignment [IssuedDeviceAdministration.yaml:141], QuestionAssignment [IssuedDeviceAdministration.yaml:247], BiometricAssignment [IssuedDeviceAdministration.yaml:407], DeviceAssignment [IssuedDeviceAdministration.yaml:433], ReaderAssignment [IssuedDeviceAdministration.yaml:672], ChequesAssignment [IssuedDeviceAdministration.yaml:803], TokenAssignment [IssuedDeviceAdministration.yaml:856]
- **Operations (39):** Capture 5, Control 7, Exchange 5, Execute 1, Initiate 5, Provide 1, Retrieve 8, Update 7 [IssuedDeviceAdministration.yaml:12]
- **Schemas:** 74 total, 15 domain-specific, 59 shared-across-≥10-specs
- **Event channels:** 16 (e.g. `IssuedDeviceAllocation/Created`) [asyncapi:IssuedDeviceAdministration.yaml:14]

## Issued Device Tracking

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/IssuedDeviceTracking.yaml` (sha256 `d9a90c49134e…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: IssuedDeviceTracking.yaml`
- **Purpose (verbatim from spec):** This service domain handles operational access to issued device tracking services. Services report on the status of devices such as cards, fobs, etc. that have been issued to customers. Service notifications include fraud warnings/alerts and device cancellation. [IssuedDeviceTracking.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`Device` in title); Cards & Merchant Services (`cards` in description); Risk, Compliance & Fraud (`fraud` in description); Customer, Sales & Marketing (`customer` in description); Reference & Data Management (`report` in description) [IssuedDeviceTracking.yaml:3]
- **Control Record:** IssuedDeviceState [IssuedDeviceTracking.yaml:15]
- **Behavior Qualifiers (2):** InternalNotification [IssuedDeviceTracking.yaml:41], ExternalReport [IssuedDeviceTracking.yaml:66]
- **Operations (10):** Capture 2, Control 1, Initiate 1, Retrieve 3, Update 3 [IssuedDeviceTracking.yaml:12]
- **Schemas:** 27 total, 3 domain-specific, 24 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `IssuedDeviceState/Created`) [asyncapi:IssuedDeviceTracking.yaml:12]

## Knowledge Exchange

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/KnowledgeExchange.yaml` (sha256 `c7f769e01d39…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: KnowledgeExchange.yaml`
- **Purpose (verbatim from spec):** Consolidate, classify and provide structured access to consolidated market intelligence, product and procedural knowledge gained from the workforce in the execution of business to inform business activity and support continual improvement [KnowledgeExchange.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`market` in description); Customer, Sales & Marketing (`product` in description); Corporate Operations & Support (`workforce` in description) [KnowledgeExchange.yaml:4]
- **Control Record:** IntellectualPropertyExchangeOperatingSession [KnowledgeExchange.yaml:15]
- **Behavior Qualifiers (5):** IndexingandPublication [KnowledgeExchange.yaml:141], CaptureandClassification [KnowledgeExchange.yaml:168], Review_RefinementandEditing [KnowledgeExchange.yaml:300], Archiving [KnowledgeExchange.yaml:404], MaintenanceandAccessAdministration [KnowledgeExchange.yaml:429]
- **Operations (23):** Control 1, Exchange 4, Execute 2, Initiate 2, Request 3, Retrieve 6, Update 5 [KnowledgeExchange.yaml:12]
- **Schemas:** 39 total, 7 domain-specific, 32 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `IntellectualPropertyExchangeOperatingSession/Created`) [asyncapi:KnowledgeExchange.yaml:11]

## Lead and Opportunity Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/LeadandOpportunityManagement.yaml` (sha256 `2843f2804397…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: LeadandOpportunityManagement.yaml`
- **Purpose (verbatim from spec):** This service domain captures, classifies and track sales lead/opportunities with established clients for additional products or services. It handles the processing of the opportunity through to the point of formal offer processing. [LeadandOpportunityManagement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Lead` in title); Corporate Operations & Support (`service` in description) [LeadandOpportunityManagement.yaml:3]
- **Control Record:** LeadandOpportunityProcedure [LeadandOpportunityManagement.yaml:15]
- **Behavior Qualifiers (1):** Development [LeadandOpportunityManagement.yaml:141]
- **Operations (10):** Control 1, Exchange 1, Execute 1, Initiate 2, Request 1, Retrieve 2, Update 2 [LeadandOpportunityManagement.yaml:12]
- **Schemas:** 42 total, 5 domain-specific, 37 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `LeadandOpportunityProcedure/Created`) [asyncapi:LeadandOpportunityManagement.yaml:11]

## Leasing

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/Leasing.yaml` (sha256 `f3046ba11239…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: Leasing.yaml`
- **Purpose (verbatim from spec):** The leasing products enables customers to finance equipment purchases using the leased item as collateral when necessary [Leasing.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Leasing` in title); Customer, Sales & Marketing (`product` in description) [Leasing.yaml:3]
- **Control Record:** LeasingFacility [Leasing.yaml:15]
- **Behavior Qualifiers (11):** Charge [Leasing.yaml:193], Payment [Leasing.yaml:220], Sweep [Leasing.yaml:247], Deposit [Leasing.yaml:274], CollateralAllocation [Leasing.yaml:300], CorporateAction [Leasing.yaml:326], IssuedDevice [Leasing.yaml:352], FinancialStatusTracking [Leasing.yaml:430], DebitandCredit [Leasing.yaml:482], Interest [Leasing.yaml:633], AmountBlock [Leasing.yaml:1082]
- **Operations (44):** Control 1, Exchange 4, Execute 1, Initiate 11, Request 3, Retrieve 12, Update 12 [Leasing.yaml:12]
- **Schemas:** 235 total, 32 domain-specific, 203 shared-across-≥10-specs
- **Event channels:** 26 (e.g. `LeasingFacility/Created`) [asyncapi:Leasing.yaml:10]

## Leasing Item Administration

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/LeasingItemAdministration.yaml` (sha256 `b40bb99329ec…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: LeasingItemAdministration.yaml`
- **Purpose (verbatim from spec):** Track the status of the assets underlying leasing agreements as they represent collateral items that could be accessed in the event of account recovery [LeasingItemAdministration.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Leasing` in title); Deposits & Accounts (`account` in description) [LeasingItemAdministration.yaml:3]
- **Control Record:** LeasingItemAdministrativePlan [LeasingItemAdministration.yaml:15]
- **Behavior Qualifiers (3):** Assurance [LeasingItemAdministration.yaml:219], ItemRegistration [LeasingItemAdministration.yaml:246], Valuation [LeasingItemAdministration.yaml:273]
- **Operations (20):** Capture 4, Control 1, Exchange 1, Grant 1, Initiate 4, Request 1, Retrieve 4, Update 4 [LeasingItemAdministration.yaml:12]
- **Schemas:** 64 total, 7 domain-specific, 57 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `LeasingItemAdministrativePlan/Created`) [asyncapi:LeasingItemAdministration.yaml:10]
- **Other domains named in this purpose text:** Account Recovery [LeasingItemAdministration.yaml:4]

## Legal Advisory

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/LegalAdvisory.yaml` (sha256 `66fb4ba23ff6…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: LegalAdvisory.yaml`
- **Purpose (verbatim from spec):** The role of the Service Domain is to provide customers and bank employees with advice on legal aspects of product sales and servicing as well as on planned and executed transactions. [LegalAdvisory.yaml:4]
- **Theme [derived-rule]:** primary Risk, Compliance & Fraud; all matches: Risk, Compliance & Fraud (`Legal` in title); Customer, Sales & Marketing (`customer` in description); Channels & Servicing (`servicing` in description); Corporate Operations & Support (`Service` in description) [LegalAdvisory.yaml:3]
- **Behavior Qualifiers:** none
- **Operations:** none defined (the OpenAPI `paths` section is empty or absent)
- **Schemas:** 4 total, 2 domain-specific, 2 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `LegalAdvice/Created`) [asyncapi:LegalAdvisory.yaml:11]

## Legal Compliance

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/LegalCompliance.yaml` (sha256 `6a96018e105c…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: LegalCompliance.yaml`
- **Purpose (verbatim from spec):** Provide specialist legal advice, assess for legal compliance and resolve legal cases as they occur [LegalCompliance.yaml:4]
- **Theme [derived-rule]:** primary Risk, Compliance & Fraud; all matches: Risk, Compliance & Fraud (`Legal` in title) [LegalCompliance.yaml:3]
- **Control Record:** LegalComplianceAssessment [LegalCompliance.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (5):** Evaluate 1, Exchange 1, Request 1, Retrieve 1, Update 1 [LegalCompliance.yaml:12]
- **Schemas:** 127 total, 2 domain-specific, 125 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `LegalComplianceAssessment/Created`) [asyncapi:LegalCompliance.yaml:9]

## Legal Entity Directory

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/LegalEntityDirectory.yaml` (sha256 `6c38eb742ed1…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: LegalEntityDirectory.yaml`
- **Purpose (verbatim from spec):** This service domain maintains details of the legal entity structure of the party including dependents and associations for individuals and ownership/subsidiary structures for corporations. Some financial indicators and product coverage/activity details can be included where this defines the nature… [LegalEntityDirectory.yaml:4]
- **Theme [derived-rule]:** primary Risk, Compliance & Fraud; all matches: Risk, Compliance & Fraud (`Legal` in title); Reference & Data Management (`Directory` in title); Customer, Sales & Marketing (`party` in description); Finance, Accounting & Treasury (`financial` in description); Corporate Operations & Support (`service` in description) [LegalEntityDirectory.yaml:3]
- **Control Record:** LegalEntityDirectoryEntry [LegalEntityDirectory.yaml:15]
- **Behavior Qualifiers (3):** Reference [LegalEntityDirectory.yaml:143], Profile [LegalEntityDirectory.yaml:221], Associations [LegalEntityDirectory.yaml:273]
- **Operations (13):** Control 1, Exchange 1, Execute 1, Register 1, Request 1, Retrieve 4, Update 4 [LegalEntityDirectory.yaml:12]
- **Schemas:** 41 total, 4 domain-specific, 37 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `LegalEntityDirectoryEntry/Created`) [asyncapi:LegalEntityDirectory.yaml:13]

## Letter of Credit

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/LetterofCredit.yaml` (sha256 `56223a125078…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: LetterofCredit.yaml`
- **Purpose (verbatim from spec):** This Service Domain handles the pricing and issuance of letters of credit to its corporate customers in support of their international trading requirements [LetterofCredit.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Credit` in title); Securities, Trading & Markets (`trading` in description); Customer, Sales & Marketing (`customer` in description); Reference & Data Management (`pricing` in description); Corporate Operations & Support (`Service` in description) [LetterofCredit.yaml:3]
- **Control Record:** LetterOfCreditTransaction [LetterofCredit.yaml:15]
- **Behavior Qualifiers (6):** CustomerCollateralAllocation [LetterofCredit.yaml:217], LetterofCreditIssuance [LetterofCredit.yaml:244], CustomerPayment [LetterofCredit.yaml:271], LetterofCreditDefinitionandPricing [LetterofCredit.yaml:298], SellerObligationConfirmation [LetterofCredit.yaml:325], LetterofCreditDemandPayment [LetterofCredit.yaml:352]
- **Operations (50):** Control 1, Exchange 7, Execute 7, Initiate 7, Notify 7, Request 7, Retrieve 7, Update 7 [LetterofCredit.yaml:12]
- **Schemas:** 201 total, 39 domain-specific, 162 shared-across-≥10-specs
- **Event channels:** 27 (e.g. `LetterOfCreditTransaction/Created`) [asyncapi:LetterofCredit.yaml:10]

## Loan

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/Loan.yaml` (sha256 `a456d6404139…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: Loan.yaml`
- **Purpose (verbatim from spec):** This service domain handles the fulfillment of a general loan product. This includes the initial set-up of the loan facility and the completion of scheduled and ad-hoc product processing tasks [Loan.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Loan` in title); Customer, Sales & Marketing (`product` in description); Corporate Operations & Support (`service` in description) [Loan.yaml:3]
- **Control Record:** LoanFacility [Loan.yaml:15]
- **Behavior Qualifiers (7):** Charge [Loan.yaml:115], Interest [Loan.yaml:142], Disbursement [Loan.yaml:192], DebitandCredit [Loan.yaml:217], Maintenance [Loan.yaml:323], Repayment [Loan.yaml:375], Modification [Loan.yaml:481]
- **Operations (24):** Control 1, Exchange 1, Execute 4, Initiate 2, Request 4, Retrieve 8, Update 4 [Loan.yaml:12]
- **Schemas:** 200 total, 24 domain-specific, 176 shared-across-≥10-specs
- **Event channels:** 18 (e.g. `LoanFacility/Created`) [asyncapi:Loan.yaml:11]

## Loan Syndication

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/LoanSyndication.yaml` (sha256 `52ccad641656…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: LoanSyndication.yaml`
- **Purpose (verbatim from spec):** Loan Syndication is a Service Domain that supports orgination, set-up and servicing of syndicated loans. It provides services that are used in lead banks, agents and banks providing administrative support. It handles the orchestration of origination and servicing processes for syndicated loans. [LoanSyndication.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Loan` in title); Customer, Sales & Marketing (`lead` in description); Channels & Servicing (`servicing` in description); Corporate Operations & Support (`Service` in description) [LoanSyndication.yaml:3]
- **Control Record:** SyndicatedLoanApplicationProcedure [LoanSyndication.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (4):** Control 1, Initiate 1, Retrieve 1, Update 1 [LoanSyndication.yaml:12]
- **Schemas:** 63 total, 1 domain-specific, 62 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `SyndicatedLoanApplicationProcedure/Created`) [asyncapi:LoanSyndication.yaml:14]

## Location Data Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/LocationDataManagement.yaml` (sha256 `d3ea08295ae7…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: LocationDataManagement.yaml`
- **Purpose (verbatim from spec):** This service domain maintain details of the use and state of locations of interest to the bank. This can include both physical and virtual addresses. It is used to check for valid use and for sales/marketing activities [LocationDataManagement.yaml:4]
- **Theme [derived-rule]:** primary Reference & Data Management; all matches: Reference & Data Management (`Data` in title); Securities, Trading & Markets (`market` in description); Customer, Sales & Marketing (`sales` in description); Corporate Operations & Support (`service` in description) [LocationDataManagement.yaml:3]
- **Control Record:** LocationDirectoryEntry [LocationDataManagement.yaml:15]
- **Behavior Qualifiers (3):** Location [LocationDataManagement.yaml:193], Use [LocationDataManagement.yaml:272], Occupancy [LocationDataManagement.yaml:324]
- **Operations (14):** Control 1, Exchange 2, Execute 1, Register 1, Request 1, Retrieve 4, Update 4 [LocationDataManagement.yaml:12]
- **Schemas:** 25 total, 6 domain-specific, 19 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `LocationDirectoryEntry/Created`) [asyncapi:LocationDataManagement.yaml:11]

## Management Manual

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ManagementManual.yaml` (sha256 `88945f8ff20b…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: ManagementManual.yaml`
- **Purpose (verbatim from spec):** Develop, maintain and promulgate the management manual of required procedures and guidelines. Provide support in its reference and interpretation as appropriate [ManagementManual.yaml:4]
- **Theme [derived-rule]:** primary Reference & Data Management; all matches: Reference & Data Management (`reference` in description) [ManagementManual.yaml:4]
- **Control Record:** ManagementManualSpecification [ManagementManual.yaml:15]
- **Behavior Qualifiers (6):** CompanyMissionandPolicies [ManagementManual.yaml:117], EmploymentRelatedProceduresandGuidelines [ManagementManual.yaml:220], LegalandRegulatoryObligationsandGuidelines [ManagementManual.yaml:299], OperationalSecurityProceduresandGuidelines [ManagementManual.yaml:326], OperationalandProductionProceduresandGuidelines [ManagementManual.yaml:353], StaffManagementProceduresandGuidelines [ManagementManual.yaml:380]
- **Operations (31):** Capture 7, Control 1, Exchange 1, Initiate 7, Request 1, Retrieve 7, Update 7 [ManagementManual.yaml:12]
- **Schemas:** 31 total, 8 domain-specific, 23 shared-across-≥10-specs
- **Event channels:** 16 (e.g. `ManagementManualSpecification/Created`) [asyncapi:ManagementManual.yaml:10]

## Market Analysis

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/MarketAnalysis.yaml` (sha256 `836472e947e0…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: MarketAnalysis.yaml`
- **Purpose (verbatim from spec):** This service domain analyzes internal and external market information sources as necessary to develop specific market insights. It may maintain a collection of predefined market analyses and may also offer specific ad-hoc analysis on request [MarketAnalysis.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Market` in title); Customer, Sales & Marketing (`offer` in description); Reference & Data Management (`information` in description); Corporate Operations & Support (`service` in description) [MarketAnalysis.yaml:3]
- **Control Record:** GeneralMarketResearchAnalysis [MarketAnalysis.yaml:15]
- **Behavior Qualifiers (1):** CompetitiveAnalysis [MarketAnalysis.yaml:115]
- **Operations (5):** Evaluate 2, Execute 1, Request 1, Retrieve 1 [MarketAnalysis.yaml:12]
- **Schemas:** 41 total, 13 domain-specific, 28 shared-across-≥10-specs
- **Event channels:** 16 (e.g. `GeneralMarketResearchAnalysis/Created`) [asyncapi:MarketAnalysis.yaml:11]

## Market Data Switch Operation

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/MarketDataSwitchOperation.yaml` (sha256 `3a76133d50d6…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: MarketDataSwitchOperation.yaml`
- **Purpose (verbatim from spec):** This service domain operates the internal information distribution facility/switch in compliance with administered external subscription information feed service access rights. Note the content is retrieved by the Market Feed Operation service domain from the various external feed services. Interna… [MarketDataSwitchOperation.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Market` in title); Reference & Data Management (`Data` in title); Risk, Compliance & Fraud (`complian` in description); Corporate Operations & Support (`service` in description) [MarketDataSwitchOperation.yaml:3]
- **Control Record:** InformationFeedSwitchOperatingSession [MarketDataSwitchOperation.yaml:15]
- **Behavior Qualifiers (3):** FeedUpload [MarketDataSwitchOperation.yaml:167], InternalPublication [MarketDataSwitchOperation.yaml:246], Distribution [MarketDataSwitchOperation.yaml:351]
- **Operations (18):** Control 1, Exchange 2, Execute 2, Initiate 3, Request 2, Retrieve 4, Update 4 [MarketDataSwitchOperation.yaml:12]
- **Schemas:** 31 total, 4 domain-specific, 27 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `InformationFeedSwitchOperatingSession/Created`) [asyncapi:MarketDataSwitchOperation.yaml:14]

## Market Information Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/MarketInformationManagement.yaml` (sha256 `e96e7e8e1491…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: MarketInformationManagement.yaml`
- **Purpose (verbatim from spec):** Market information management consolidates and improves market information from multiple sources in order to build up a bank knowledge base in targeted areas [MarketInformationManagement.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Market` in title); Reference & Data Management (`Information` in title) [MarketInformationManagement.yaml:3]
- **Control Record:** FinancialMarketInformationAdministrativePlan [MarketInformationManagement.yaml:15]
- **Behavior Qualifiers (3):** Improvement [MarketInformationManagement.yaml:119], Reporting [MarketInformationManagement.yaml:144], Consolidation [MarketInformationManagement.yaml:248]
- **Operations (16):** Capture 1, Control 1, Create 2, Exchange 1, Execute 2, Grant 1, Request 2, Retrieve 4, Update 2 [MarketInformationManagement.yaml:12]
- **Schemas:** 31 total, 7 domain-specific, 24 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `FinancialMarketInformationAdministrativePlan/Created`) [asyncapi:MarketInformationManagement.yaml:10]

## Market Making

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/MarketMaking.yaml` (sha256 `7e629bcf45f6…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: MarketMaking.yaml`
- **Purpose (verbatim from spec):** This Service Domain enables the bank to fulfill its market making function typically in collaboration with a trading exchange. The bank maintains a buy/sell quote for the securities it supports as a market maker and accepts buy/sell orders on request [MarketMaking.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Market` in title); Corporate Operations & Support (`Service` in description) [MarketMaking.yaml:3]
- **Control Record:** MarketMakingFacility [MarketMaking.yaml:15]
- **Behavior Qualifiers (3):** Quote [MarketMaking.yaml:191], Order [MarketMaking.yaml:218], PositionTracking [MarketMaking.yaml:272]
- **Operations (29):** Control 1, Exchange 4, Execute 4, Initiate 4, Notify 4, Request 4, Retrieve 4, Update 4 [MarketMaking.yaml:12]
- **Schemas:** 127 total, 7 domain-specific, 120 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `MarketMakingFacility/Created`) [asyncapi:MarketMaking.yaml:12]

## Market Order

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/MarketOrder.yaml` (sha256 `35b9fa506738…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: MarketOrder.yaml`
- **Purpose (verbatim from spec):** Market Order records an instruction from a customer or his or her representative to buy or sell securities. It follows the order during its lifetime and reports back to the requestor on the execution. [MarketOrder.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Market` in title); Customer, Sales & Marketing (`customer` in description); Reference & Data Management (`report` in description); Corporate Operations & Support (`record` in description) [MarketOrder.yaml:3]
- **Control Record:** MarketOrderTransaction [MarketOrder.yaml:15]
- **Behavior Qualifiers (4):** Confirmation [MarketOrder.yaml:65], Quote [MarketOrder.yaml:90], Compliance [MarketOrder.yaml:115], TradeInitiation [MarketOrder.yaml:164]
- **Operations (8):** Exchange 1, Initiate 1, Retrieve 5, Update 1 [MarketOrder.yaml:12]
- **Schemas:** 46 total, 9 domain-specific, 37 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `MarketOrderTransaction/Created`) [asyncapi:MarketOrder.yaml:11]

## Market Order Execution

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/MarketOrderExecution.yaml` (sha256 `c6f23d0dc547…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: MarketOrderExecution.yaml`
- **Purpose (verbatim from spec):** The Market Order Execution Service Domain is responsible for the booking of securities transactions (e.g. resulting from market orders or some types of corporate actions) on investment accounts, so in terms of security name plus quantity. [MarketOrderExecution.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Market` in title); Deposits & Accounts (`account` in description); Corporate Operations & Support (`Service` in description) [MarketOrderExecution.yaml:3]
- **Control Record:** MarketTradeTransaction [MarketOrderExecution.yaml:15]
- **Behavior Qualifiers (3):** Position [MarketOrderExecution.yaml:91], TradeInitiation [MarketOrderExecution.yaml:118], Quote [MarketOrderExecution.yaml:195]
- **Operations (16):** Control 1, Exchange 2, Execute 1, Initiate 3, Request 3, Retrieve 4, Update 2 [MarketOrderExecution.yaml:12]
- **Schemas:** 47 total, 7 domain-specific, 40 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `MarketTradeTransaction/Created`) [asyncapi:MarketOrderExecution.yaml:11]
- **Other domains named in this purpose text:** Market Order [MarketOrderExecution.yaml:4]

## Market Research

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/MarketResearch.yaml` (sha256 `a9aeb91c71fb…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: MarketResearch.yaml`
- **Purpose (verbatim from spec):** This service domain handles the capture of market research from multiple external sources. This can include live feeds, analysis and reports in any form. The information is classified/catalogued and stored for retrieval. [MarketResearch.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Market` in title); Reference & Data Management (`report` in description); Corporate Operations & Support (`service` in description) [MarketResearch.yaml:3]
- **Control Record:** GeneralMarketResearchDirectoryEntry [MarketResearch.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (5):** Execute 1, Register 1, Request 1, Retrieve 1, Update 1 [MarketResearch.yaml:12]
- **Schemas:** 66 total, 28 domain-specific, 38 shared-across-≥10-specs
- **Event channels:** 32 (e.g. `GeneralMarketResearchDirectoryEntry/Created`) [asyncapi:MarketResearch.yaml:11]

## Merchandising Loan

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/MerchandisingLoan.yaml` (sha256 `4ec4c964d789…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: MerchandisingLoan.yaml`
- **Purpose (verbatim from spec):** Fulfillment of loan product used in the purchase of a larger merchandise item such as a car or boat. The purchased item is typically treated as collateral for the loan [MerchandisingLoan.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Loan` in title); Customer, Sales & Marketing (`product` in description) [MerchandisingLoan.yaml:3]
- **Control Record:** MerchandisingLoanFacility [MerchandisingLoan.yaml:15]
- **Behavior Qualifiers (12):** Billing [MerchandisingLoan.yaml:193], Charge [MerchandisingLoan.yaml:220], Payment [MerchandisingLoan.yaml:247], Sweep [MerchandisingLoan.yaml:274], CollateralAllocation [MerchandisingLoan.yaml:327], Deposit [MerchandisingLoan.yaml:379], IssuedDevice [MerchandisingLoan.yaml:405], DebitandCredit [MerchandisingLoan.yaml:483], Booking [MerchandisingLoan.yaml:609], Interest [MerchandisingLoan.yaml:634], FinancialStatusTracking [MerchandisingLoan.yaml:1137], AmountBlock [MerchandisingLoan.yaml:1164]
- **Operations (47):** Control 1, Exchange 5, Execute 4, Initiate 10, Request 3, Retrieve 12, Update 12 [MerchandisingLoan.yaml:12]
- **Schemas:** 235 total, 33 domain-specific, 202 shared-across-≥10-specs
- **Event channels:** 28 (e.g. `MerchandisingLoanFacility/Created`) [asyncapi:MerchandisingLoan.yaml:10]

## Merchant Acquiring Facility

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/MerchantAcquiringFacility.yaml` (sha256 `2f21ef4bd832…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: MerchantAcquiringFacility.yaml`
- **Purpose (verbatim from spec):** This service domain orchestrates the activities related to Merchant fulfillment, Merchant Account maintenance, Merchant transactional activities and settlement, including the billing of merchant fees and charges. [MerchantAcquiringFacility.yaml:4]
- **Theme [derived-rule]:** primary Cards & Merchant Services; all matches: Cards & Merchant Services (`Merchant` in title); Corporate Operations & Support (`Facilit` in title); Payments & Settlement (`settle` in description); Deposits & Accounts (`Account` in description); Finance, Accounting & Treasury (`billing` in description) [MerchantAcquiringFacility.yaml:3]
- **Control Record:** MerchantAcquiringFacility [MerchantAcquiringFacility.yaml:15]
- **Behavior Qualifiers (5):** SupportFacility [MerchantAcquiringFacility.yaml:117], Clearing [MerchantAcquiringFacility.yaml:166], Charge [MerchantAcquiringFacility.yaml:220], Chargeback [MerchantAcquiringFacility.yaml:247], Settlement [MerchantAcquiringFacility.yaml:274]
- **Operations (19):** Control 1, Exchange 1, Execute 4, Initiate 1, Request 1, Retrieve 6, Update 5 [MerchantAcquiringFacility.yaml:12]
- **Schemas:** 186 total, 15 domain-specific, 171 shared-across-≥10-specs
- **Event channels:** 12 (e.g. `MerchantAcquiringFacility/Created`) [asyncapi:MerchantAcquiringFacility.yaml:11]

## Merchant Relations

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/MerchantRelations.yaml` (sha256 `973b2cb3f997…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: MerchantRelations.yaml`
- **Purpose (verbatim from spec):** This service domain maintains the terms and conditions agreed with merchants for cards related activity [MerchantRelations.yaml:4]
- **Theme [derived-rule]:** primary Cards & Merchant Services; all matches: Cards & Merchant Services (`Merchant` in title); Corporate Operations & Support (`service` in description) [MerchantRelations.yaml:3]
- **Control Record:** MerchantRelationshipAgreement [MerchantRelations.yaml:15]
- **Behavior Qualifiers (3):** OperationalTerm [MerchantRelations.yaml:41], RegulatoryTerm [MerchantRelations.yaml:91], LegalTerm [MerchantRelations.yaml:144]
- **Operations (26):** Control 1, Evaluate 4, Exchange 4, Grant 1, Notify 4, Request 4, Retrieve 4, Update 4 [MerchantRelations.yaml:12]
- **Schemas:** 118 total, 9 domain-specific, 109 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `MerchantRelationshipAgreement/Created`) [asyncapi:MerchantRelations.yaml:10]

## Mergers and Acquisitions Advisory

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/MergersandAcquisitionsAdvisory.yaml` (sha256 `b20c0a2001c0…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: MergersandAcquisitionsAdvisory.yaml`
- **Purpose (verbatim from spec):** This Service Domain handles mergers and acquisition, IPO, MBO and LBO projects with the bank acting in the lead and/or subordinate role [MergersandAcquisitionsAdvisory.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`lead` in description); Corporate Operations & Support (`Service` in description) [MergersandAcquisitionsAdvisory.yaml:4]
- **Control Record:** MergersAndAcquisitionAdvice [MergersandAcquisitionsAdvisory.yaml:42]
- **Behavior Qualifiers (1):** MergerandAcquisition [MergersandAcquisitionsAdvisory.yaml:15]
- **Operations (15):** Control 1, Exchange 2, Execute 2, Initiate 2, Notify 2, Request 2, Retrieve 2, Update 2 [MergersandAcquisitionsAdvisory.yaml:12]
- **Schemas:** 47 total, 6 domain-specific, 41 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `MergersAndAcquisitionAdvice/Created`) [asyncapi:MergersandAcquisitionsAdvisory.yaml:10]

## Mortgage Loan

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/MortgageLoan.yaml` (sha256 `7591a25f593a…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: MortgageLoan.yaml`
- **Purpose (verbatim from spec):** Fulfillment of a loan product for the purpose of property purchase. Note different servicing patterns can be applied to interest calculations and principle and interest repayments [MortgageLoan.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Mortgage` in title); Payments & Settlement (`payment` in description); Customer, Sales & Marketing (`product` in description); Channels & Servicing (`servicing` in description); Corporate Operations & Support (`property` in description) [MortgageLoan.yaml:3]
- **Control Record:** MortgageLoanFacility [MortgageLoan.yaml:15]
- **Behavior Qualifiers (12):** Billing [MortgageLoan.yaml:193], Charge [MortgageLoan.yaml:220], Payment [MortgageLoan.yaml:247], Sweep [MortgageLoan.yaml:274], Deposit [MortgageLoan.yaml:327], CollateralAllocation [MortgageLoan.yaml:379], IssuedDevice [MortgageLoan.yaml:405], DebitandCredit [MortgageLoan.yaml:457], Booking [MortgageLoan.yaml:609], Interest [MortgageLoan.yaml:634], FinancialStatusTracking [MortgageLoan.yaml:1137], AmountBlock [MortgageLoan.yaml:1164]
- **Operations (47):** Control 1, Exchange 5, Execute 4, Initiate 10, Request 3, Retrieve 12, Update 12 [MortgageLoan.yaml:12]
- **Schemas:** 236 total, 33 domain-specific, 203 shared-across-≥10-specs
- **Event channels:** 28 (e.g. `MortgageLoanFacility/Created`) [asyncapi:MortgageLoan.yaml:11]

## Mutual Fund Administration

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/MutualFundAdministration.yaml` (sha256 `3014968a2d7f…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: MutualFundAdministration.yaml`
- **Purpose (verbatim from spec):** The Mutual Fund Administration Service Domain handles all aspects of the set-up and operation of mutual funds that can be offered to the bank's general (non-accredited) customers [MutualFundAdministration.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Fund` in title); Lending & Credit (`credit` in description); Customer, Sales & Marketing (`customer` in description); Corporate Operations & Support (`Service` in description) [MutualFundAdministration.yaml:3]
- **Control Record:** MutualFundAdministrativePlan [MutualFundAdministration.yaml:15]
- **Behavior Qualifiers (8):** FundAccounting [MutualFundAdministration.yaml:217], FundDevelopment [MutualFundAdministration.yaml:244], FundEnrolment [MutualFundAdministration.yaml:271], FundFinancialReporting [MutualFundAdministration.yaml:298], FundInflowsandOutflow [MutualFundAdministration.yaml:325], FundInvestor_MiddleandBackOfficeService [MutualFundAdministration.yaml:352], FundManagementFee [MutualFundAdministration.yaml:379], FundTaxAdministration [MutualFundAdministration.yaml:406]
- **Operations (56):** Control 1, Create 1, Exchange 9, Grant 9, Notify 9, Request 9, Retrieve 9, Update 9 [MutualFundAdministration.yaml:12]
- **Schemas:** 73 total, 11 domain-specific, 62 shared-across-≥10-specs
- **Event channels:** 29 (e.g. `MutualFundAdministrativePlan/Created`) [asyncapi:MutualFundAdministration.yaml:11]

## Notional Pooling

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/NotionalPooling.yaml` (sha256 `f6ec9f889036…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: NotionalPooling.yaml`
- **Purpose (verbatim from spec):** Notional pooling allows corporate customer with multiple active accounts to pool credit and debit balances to provide a single centralized liquidity position and to minimize interest expense, simplify cash management and retain a degree of local autonomy to the accounts [NotionalPooling.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`credit` in description); Securities, Trading & Markets (`position` in description); Deposits & Accounts (`account` in description); Customer, Sales & Marketing (`customer` in description); Finance, Accounting & Treasury (`cash` in description) [NotionalPooling.yaml:4]
- **Control Record:** NotionalPoolingFacility [NotionalPooling.yaml:15]
- **Behavior Qualifiers (1):** CashTransfer [NotionalPooling.yaml:165]
- **Operations (15):** Control 1, Exchange 2, Execute 2, Initiate 2, Notify 2, Request 2, Retrieve 2, Update 2 [NotionalPooling.yaml:12]
- **Schemas:** 123 total, 3 domain-specific, 120 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `NotionalPoolingFacility/Created`) [asyncapi:NotionalPooling.yaml:12]

## Open Item Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/OpenItemManagement.yaml` (sha256 `0c7a035f44b4…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: OpenItemManagement.yaml`
- **Purpose (verbatim from spec):** This service domain provides a service for handling the resolution of open items against accounts (such as overdue loan payments) [OpenItemManagement.yaml:4]
- **Theme [derived-rule]:** primary Payments & Settlement; all matches: Payments & Settlement (`payment` in description); Lending & Credit (`loan` in description); Deposits & Accounts (`account` in description); Corporate Operations & Support (`service` in description) [OpenItemManagement.yaml:4]
- **Control Record:** OpenItemProcedure [OpenItemManagement.yaml:15]
- **Behavior Qualifiers (2):** Tracking [OpenItemManagement.yaml:117], Repayment [OpenItemManagement.yaml:166]
- **Operations (11):** Control 1, Exchange 1, Execute 1, Initiate 2, Request 1, Retrieve 3, Update 2 [OpenItemManagement.yaml:12]
- **Schemas:** 44 total, 7 domain-specific, 37 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `OpenItemProcedure/Created`) [asyncapi:OpenItemManagement.yaml:10]

## Operational Gateway

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/OperationalGateway.yaml` (sha256 `e997bc841d76…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: OperationalGateway.yaml`
- **Purpose (verbatim from spec):** This Service Domain operates production information exchanges with external parties for non-financial messages/transactions. It may employ a broad range of channels, media and technologies as needed to support the different requirements of any particular third party interface [OperationalGateway.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`product` in description); Channels & Servicing (`channel` in description); Finance, Accounting & Treasury (`financial` in description); Reference & Data Management (`information` in description); Corporate Operations & Support (`Service` in description) [OperationalGateway.yaml:4]
- **Control Record:** OperationalGatewayOperatingSession [OperationalGateway.yaml:15]
- **Behavior Qualifiers (3):** InboundMessage [OperationalGateway.yaml:193], OutboundWithResponse [OperationalGateway.yaml:244], OutboundMessage [OperationalGateway.yaml:297]
- **Operations (29):** Control 1, Exchange 4, Execute 4, Initiate 4, Notify 4, Request 4, Retrieve 4, Update 4 [OperationalGateway.yaml:12]
- **Schemas:** 35 total, 5 domain-specific, 30 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `OperationalGatewayOperatingSession/Created`) [asyncapi:OperationalGateway.yaml:12]

## Operations Log

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/OperationsLog.yaml` (sha256 `ba2b3d5298a5…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: OperationsLog.yaml`
- **Purpose (verbatim from spec):** This service domain handle the day-to-day operations of a collaborative partner related services. [OperationsLog.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`service` in description) [OperationsLog.yaml:4]
- **Behavior Qualifiers:** none
- **Operations:** none defined (the OpenAPI `paths` section is empty or absent)
- **Schemas:** 2 total, 1 domain-specific, 1 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `PartnerEventLog/Created`) [asyncapi:OperationsLog.yaml:9]

## Order Allocation

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/OrderAllocation.yaml` (sha256 `f46a130c3a1e…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: OrderAllocation.yaml`
- **Purpose (verbatim from spec):** This Service Domain allocates partially fulfilled market trades [OrderAllocation.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`market` in description); Corporate Operations & Support (`Service` in description) [OrderAllocation.yaml:4]
- **Control Record:** SecuritiesAllocationProcedure [OrderAllocation.yaml:15]
- **Behavior Qualifiers (2):** ApplyOrderAllocationRules [OrderAllocation.yaml:217], Update(PartiallyCompleted)MarketOrder [OrderAllocation.yaml:244]
- **Operations (22):** Control 1, Exchange 3, Execute 3, Initiate 3, Notify 3, Request 3, Retrieve 3, Update 3 [OrderAllocation.yaml:12]
- **Schemas:** 75 total, 4 domain-specific, 71 shared-across-≥10-specs
- **Event channels:** 11 (e.g. `SecuritiesAllocationProcedure/Created`) [asyncapi:OrderAllocation.yaml:9]

## Partner Administration

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/PartnerAdministration.yaml` (sha256 `ddfd1221f6f0…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: PartnerAdministration.yaml`
- **Purpose (verbatim from spec):** This service domain handle the day-to-day operations of a collaborative partner related services. [PartnerAdministration.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`service` in description) [PartnerAdministration.yaml:4]
- **Behavior Qualifiers:** none
- **Operations:** none defined (the OpenAPI `paths` section is empty or absent)
- **Schemas:** 2 total, 1 domain-specific, 1 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `PartnerAdministrativePlan/Created`) [asyncapi:PartnerAdministration.yaml:9]

## Partner Agreement

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/PartnerAgreement.yaml` (sha256 `647a206f0a48…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: PartnerAgreement.yaml`
- **Purpose (verbatim from spec):** This service domain captures and maintains comprehensive terms and conditions govering Partner relationships. [PartnerAgreement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`relationship` in description); Corporate Operations & Support (`service` in description) [PartnerAgreement.yaml:4]
- **Control Record:** PartnerAgreement [PartnerAgreement.yaml:15]
- **Behavior Qualifiers (3):** LegalTerm [PartnerAgreement.yaml:193], RegulatoryTerm [PartnerAgreement.yaml:271], PolicyTerm [PartnerAgreement.yaml:349]
- **Operations (16):** Control 1, Evaluate 4, Exchange 1, Grant 1, Request 1, Retrieve 4, Update 4 [PartnerAgreement.yaml:12]
- **Schemas:** 28 total, 6 domain-specific, 22 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `PartnerAgreement/Created`) [asyncapi:PartnerAgreement.yaml:10]

## Partner Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/PartnerManagement.yaml` (sha256 `489b4d3c2981…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: PartnerManagement.yaml`
- **Purpose (verbatim from spec):** This service domain handles strategic management of collaborative partners including partner development, performance and relationship tracking. [PartnerManagement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`relationship` in description); Corporate Operations & Support (`service` in description) [PartnerManagement.yaml:4]
- **Behavior Qualifiers:** none
- **Operations:** none defined (the OpenAPI `paths` section is empty or absent)
- **Schemas:** 2 total, 1 domain-specific, 1 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `PartnerReleationshipManagementPlan/Created`) [asyncapi:PartnerManagement.yaml:10]

## Party Asset Directory

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/PartyAssetDirectory.yaml` (sha256 `83067035a746…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: PartyAssetDirectory.yaml`
- **Purpose (verbatim from spec):** This directory maintains reference details of assets held by a party, usually a customer of the bank. In most case, the bank's interest in the asset is because it may be pledged to the bank as collateral. [PartyAssetDirectory.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Party` in title); Reference & Data Management (`Directory` in title); Lending & Credit (`collateral` in description); Channels & Servicing (`case` in description); Corporate Operations & Support (`it` in description) [PartyAssetDirectory.yaml:3]
- **Behavior Qualifiers (4):** AssetProperties [PartyAssetDirectory.yaml:15], AssetEstimatedValue [PartyAssetDirectory.yaml:93], AssetInsurance [PartyAssetDirectory.yaml:171], AssetMaintenance [PartyAssetDirectory.yaml:197]
- **Operations (12):** Register 4, Retrieve 4, Update 4 [PartyAssetDirectory.yaml:12]
- **Schemas:** 47 total, 10 domain-specific, 37 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `PartyAssetDirectoryEntry/Created`) [asyncapi:PartyAssetDirectory.yaml:11]

## Party Authentication

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/PartyAuthentication.yaml` (sha256 `49e65556d7af…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: PartyAuthentication.yaml`
- **Purpose (verbatim from spec):** This service domain provides a customer identify authentication service covering all channels and devices to support access to the banks products and services [PartyAuthentication.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Party` in title); Channels & Servicing (`channel` in description); Corporate Operations & Support (`service` in description) [PartyAuthentication.yaml:3]
- **Control Record:** PartyAuthenticationAssessment [PartyAuthentication.yaml:15]
- **Behavior Qualifiers (6):** Password [PartyAuthentication.yaml:193], Question [PartyAuthentication.yaml:244], Document [PartyAuthentication.yaml:295], Device [PartyAuthentication.yaml:346], Biometric [PartyAuthentication.yaml:372], Behavior [PartyAuthentication.yaml:448]
- **Operations (19):** Evaluate 7, Exchange 1, Execute 1, Grant 1, Request 1, Retrieve 7, Update 1 [PartyAuthentication.yaml:12]
- **Schemas:** 61 total, 21 domain-specific, 40 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `PartyAuthenticationAssessment/Created`) [asyncapi:PartyAuthentication.yaml:10]

## Party Lifecycle Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/PartyLifecycleManagement.yaml` (sha256 `7f4c9b36e070…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: PartyLifecycleManagement.yaml`
- **Purpose (verbatim from spec):** This service domain tracks the state of a party relationship with the bank from the initial checks made during the establishment of a new party connection and subsequently maintained as necessary over the duration of the relationship. The checks and the maintenance requirements will vary by party t… [PartyLifecycleManagement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Party` in title); Corporate Operations & Support (`service` in description) [PartyLifecycleManagement.yaml:3]
- **Control Record:** PartyRelationshipAdministrativePlan [PartyLifecycleManagement.yaml:15]
- **Behavior Qualifiers (4):** Qualification [PartyLifecycleManagement.yaml:193], Documentation [PartyLifecycleManagement.yaml:218], Precedents [PartyLifecycleManagement.yaml:324], IdentityProofing [PartyLifecycleManagement.yaml:376]
- **Operations (15):** Control 1, Exchange 1, Execute 2, Initiate 1, Request 2, Retrieve 5, Update 3 [PartyLifecycleManagement.yaml:12]
- **Schemas:** 59 total, 14 domain-specific, 45 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `PartyRelationshipAdministrativePlan/Created`) [asyncapi:PartyLifecycleManagement.yaml:15]

## Party Reference Data Directory

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/PartyReferenceDataDirectory.yaml` (sha256 `fa00cf777731…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: PartyReferenceDataDirectory.yaml`
- **Purpose (verbatim from spec):** This service domain maintains a range of party reference information covering aspects including general reference details, contacts and associations and demographic information [PartyReferenceDataDirectory.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Party` in title); Reference & Data Management (`Reference` in title); Corporate Operations & Support (`service` in description) [PartyReferenceDataDirectory.yaml:3]
- **Control Record:** PartyReferenceDataDirectoryEntry [PartyReferenceDataDirectory.yaml:15]
- **Behavior Qualifiers (4):** Demographics [PartyReferenceDataDirectory.yaml:193], Reference [PartyReferenceDataDirectory.yaml:220], Associations [PartyReferenceDataDirectory.yaml:272], BankRelations [PartyReferenceDataDirectory.yaml:376]
- **Operations (17):** Control 1, Exchange 2, Execute 1, Register 2, Request 1, Retrieve 5, Update 5 [PartyReferenceDataDirectory.yaml:12]
- **Schemas:** 67 total, 19 domain-specific, 48 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `PartyReferenceDataDirectoryEntry/Created`) [asyncapi:PartyReferenceDataDirectory.yaml:11]

## Party Routing Profile

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/PartyRoutingProfile.yaml` (sha256 `4c3829463abb…`, version 14.0.0); bundle: `oas3_yamls_part4.md` under `# FILE: PartyRoutingProfile.yaml`
- **Purpose (verbatim from spec):** This service domain maintains a small profile of key indicators for a customer that is referenced during customer interactions to facilitate routing, servicing and product/service fulfillment decisions. This can include status (such as account in arrears), ratings (such as high value customer) and… [PartyRoutingProfile.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Party` in title); Deposits & Accounts (`account` in description); Channels & Servicing (`servicing` in description); Reference & Data Management (`reference` in description); Corporate Operations & Support (`service` in description) [PartyRoutingProfile.yaml:3]
- **Control Record:** PartyState [PartyRoutingProfile.yaml:15]
- **Behavior Qualifiers (3):** Status [PartyRoutingProfile.yaml:65], Rating [PartyRoutingProfile.yaml:92], Alert [PartyRoutingProfile.yaml:325]
- **Operations (18):** Capture 3, Control 1, Evaluate 1, Exchange 1, Execute 1, Initiate 1, Notify 1, Request 1, Retrieve 4, Update 4 [PartyRoutingProfile.yaml:12]
- **Schemas:** 17 total, 5 domain-specific, 12 shared-across-≥10-specs
- **Event channels:** 9 (e.g. `PartyState/Created`) [asyncapi:PartyRoutingProfile.yaml:13]

## Payment Order Initiation

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/PaymentOrderInitiation.yaml` (sha256 `d0003b3681ae…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: PaymentOrderInitiation.yaml`
- **Purpose (verbatim from spec):** This service domain provides a customer payment service. It captures the payer and payee details and other key properties of the payment and initiates the orchestration of the transaction. It provides support for repeating/scheduled payments. [PaymentOrderInitiation.yaml:4]
- **Theme [derived-rule]:** primary Payments & Settlement; all matches: Payments & Settlement (`Payment` in title); Customer, Sales & Marketing (`customer` in description); Corporate Operations & Support (`service` in description) [PaymentOrderInitiation.yaml:3]
- **Control Record:** PaymentOrderInitiationTransaction [PaymentOrderInitiation.yaml:15]
- **Behavior Qualifiers (3):** Compliance [PaymentOrderInitiation.yaml:89], Confirmation [PaymentOrderInitiation.yaml:114], OrderInitiation [PaymentOrderInitiation.yaml:139]
- **Operations (7):** Exchange 1, Initiate 1, Retrieve 4, Update 1 [PaymentOrderInitiation.yaml:12]
- **Schemas:** 137 total, 12 domain-specific, 125 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `PaymentOrderInitiationTransaction/Created`) [asyncapi:PaymentOrderInitiation.yaml:11]

## Payment Rail

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/PaymentRail.yaml` (sha256 `b135161a99ec…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: PaymentRail.yaml`
- **Purpose (verbatim from spec):** This Service Domain handles the operational interface with payment service providers, formatting outbound transactions and onward routing inbound transactions during scheduled operating sessions. It also links to holding account facilities for net payment handling [PaymentRail.yaml:4]
- **Theme [derived-rule]:** primary Payments & Settlement; all matches: Payments & Settlement (`Payment` in title); Deposits & Accounts (`account` in description); Channels & Servicing (`session` in description); Corporate Operations & Support (`Service` in description) [PaymentRail.yaml:3]
- **Control Record:** PaymentRailOperatingSession [PaymentRail.yaml:15]
- **Behavior Qualifiers (4):** InboundTransaction [PaymentRail.yaml:217], OutboundTransaction [PaymentRail.yaml:244], PaymentAccountReconciliation [PaymentRail.yaml:271], PaymentClearingandSettlement [PaymentRail.yaml:298]
- **Operations (36):** Control 1, Exchange 5, Execute 5, Initiate 5, Notify 5, Request 5, Retrieve 5, Update 5 [PaymentRail.yaml:12]
- **Schemas:** 36 total, 6 domain-specific, 30 shared-across-≥10-specs
- **Event channels:** 17 (e.g. `PaymentRailOperatingSession/Created`) [asyncapi:PaymentRail.yaml:12]

## Point of Service

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/PointofService.yaml` (sha256 `fc5535950e9a…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: PointofService.yaml`
- **Purpose (verbatim from spec):** This service domain operates servicing positions within the bank. It administers all media connections, inventory holdings (e.g. cash), provides access to support utilities and tracks servicing activity -e.g. time spent, activity logs, capturing servicing events including commission and training re… [PointofService.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`Service` in title); Securities, Trading & Markets (`position` in description); Channels & Servicing (`servicing` in description); Finance, Accounting & Treasury (`cash` in description) [PointofService.yaml:3]
- **Control Record:** PointofServiceOperatingSession [PointofService.yaml:15]
- **Behavior Qualifiers (5):** Assisted [PointofService.yaml:167], Automated [PointofService.yaml:221], Interaction [PointofService.yaml:377], Inventory [PointofService.yaml:456], CashPosition [PointofService.yaml:508]
- **Operations (23):** Control 4, Execute 3, Initiate 3, Request 1, Retrieve 6, Update 6 [PointofService.yaml:12]
- **Schemas:** 61 total, 7 domain-specific, 54 shared-across-≥10-specs
- **Event channels:** 12 (e.g. `PointofServiceOperatingSession/Created`) [asyncapi:PointofService.yaml:13]

## Position Keeping

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/PositionKeeping.yaml` (sha256 `071148a0eb25…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: PositionKeeping.yaml`
- **Purpose (verbatim from spec):** This service domain maintains a log of monetary or value transactions and entitlements log posted to product facilities. Reconciled financial transactions are subsequently used for posting to the accounting systems. [PositionKeeping.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Position` in title); Deposits & Accounts (`account` in description); Customer, Sales & Marketing (`product` in description); Finance, Accounting & Treasury (`Reconcil` in description); Corporate Operations & Support (`service` in description) [PositionKeeping.yaml:3]
- **Control Record:** FinancialPositionLog [PositionKeeping.yaml:15]
- **Behavior Qualifiers (1):** FinancialTransactionCapture [PositionKeeping.yaml:115]
- **Operations (7):** Capture 1, Control 1, Initiate 1, Retrieve 2, Update 2 [PositionKeeping.yaml:12]
- **Schemas:** 82 total, 3 domain-specific, 79 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `FinancialPositionLog/Created`) [asyncapi:PositionKeeping.yaml:11]

## Position Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/PositionManagement.yaml` (sha256 `10ab89cfaade…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: PositionManagement.yaml`
- **Purpose (verbatim from spec):** The Service Domain tracks the bank's consolidated financial positions for major customers and complex market conditions [PositionManagement.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Position` in title); Customer, Sales & Marketing (`customer` in description); Finance, Accounting & Treasury (`financial` in description); Corporate Operations & Support (`Service` in description) [PositionManagement.yaml:3]
- **Control Record:** FinancialPositionState [PositionManagement.yaml:15]
- **Behavior Qualifiers (2):** TrialTransaction [PositionManagement.yaml:117], TransactionApplication [PositionManagement.yaml:195]
- **Operations (10):** Control 1, Initiate 3, Request 1, Retrieve 2, Update 3 [PositionManagement.yaml:12]
- **Schemas:** 56 total, 6 domain-specific, 50 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `FinancialPositionState/Created`) [asyncapi:PositionManagement.yaml:10]

## Private Placement

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/PrivatePlacement.yaml` (sha256 `5287d725e788…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: PrivatePlacement.yaml`
- **Purpose (verbatim from spec):** This Service Domain provides the complete range of functions involved in providing private placement services to corporate customers. [PrivatePlacement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`customer` in description); Corporate Operations & Support (`Service` in description) [PrivatePlacement.yaml:4]
- **Control Record:** PrivatePlacementFacility [PrivatePlacement.yaml:15]
- **Behavior Qualifiers (3):** Placement [PrivatePlacement.yaml:217], Maintenance [PrivatePlacement.yaml:244], InstrumentDesign [PrivatePlacement.yaml:271]
- **Operations (29):** Control 1, Exchange 4, Execute 4, Initiate 4, Notify 4, Request 4, Retrieve 4, Update 4 [PrivatePlacement.yaml:12]
- **Schemas:** 125 total, 5 domain-specific, 120 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `PrivatePlacementFacility/Created`) [asyncapi:PrivatePlacement.yaml:10]

## Processing Order

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProcessingOrder.yaml` (sha256 `8c864037c3e3…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProcessingOrder.yaml`
- **Purpose (verbatim from spec):** The Processing Order Service Domain handles the processing of a service request that comes in via a secure channel from a known requestor, which is typically an automated process itself and not a customer. [ProcessingOrder.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`customer` in description); Channels & Servicing (`channel` in description); Corporate Operations & Support (`Service` in description) [ProcessingOrder.yaml:4]
- **Control Record:** ProcessingOrderProcedure [ProcessingOrder.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (8):** Control 1, Exchange 1, Execute 1, Initiate 1, Notify 1, Request 1, Retrieve 1, Update 1 [ProcessingOrder.yaml:12]
- **Schemas:** 66 total, 2 domain-specific, 64 shared-across-≥10-specs
- **Event channels:** 5 (e.g. `ProcessingOrderProcedure/Created`) [asyncapi:ProcessingOrder.yaml:11]

## Product Combination

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProductCombination.yaml` (sha256 `5c2c3c06353b…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProductCombination.yaml`
- **Purpose (verbatim from spec):** Product Combination supports bundled products applying necessary constraints on embedded product fulfillment and ensuring product performance analysis takes correct account of embedded products' contribution [ProductCombination.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Product` in title); Deposits & Accounts (`account` in description) [ProductCombination.yaml:3]
- **Control Record:** ProductCombinationFacility [ProductCombination.yaml:15]
- **Behavior Qualifiers (3):** Fulfillment [ProductCombination.yaml:167], TransferPricing [ProductCombination.yaml:247], SupportFacility [ProductCombination.yaml:301]
- **Operations (21):** Control 2, Exchange 3, Execute 2, Initiate 3, Request 3, Retrieve 4, Update 4 [ProductCombination.yaml:12]
- **Schemas:** 48 total, 5 domain-specific, 43 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `ProductCombinationFacility/Created`) [asyncapi:ProductCombination.yaml:11]

## Product Deployment

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProductDeployment.yaml` (sha256 `bbf1a8be301f…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProductDeployment.yaml`
- **Purpose (verbatim from spec):** Plan and administer the production deployment new and updated products and services [ProductDeployment.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Product` in title); Corporate Operations & Support (`service` in description) [ProductDeployment.yaml:3]
- **Control Record:** ProductandServiceDeploymentDevelopment [ProductDeployment.yaml:15]
- **Behavior Qualifiers (7):** Systems [ProductDeployment.yaml:219], ITOperations [ProductDeployment.yaml:325], HROperations [ProductDeployment.yaml:431], SalesandMarketing [ProductDeployment.yaml:537], Servicing [ProductDeployment.yaml:643], Production [ProductDeployment.yaml:749], ProductionSupport [ProductDeployment.yaml:830]
- **Operations (36):** Capture 1, Control 1, Create 1, Exchange 8, Grant 1, Request 8, Retrieve 8, Update 8 [ProductDeployment.yaml:12]
- **Schemas:** 64 total, 9 domain-specific, 55 shared-across-≥10-specs
- **Event channels:** 16 (e.g. `ProductandServiceDeploymentDevelopment/Created`) [asyncapi:ProductDeployment.yaml:9]

## Product Design

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProductDesign.yaml` (sha256 `feafdb1c21ed…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProductDesign.yaml`
- **Purpose (verbatim from spec):** Develop/refine product designs and supporting specification details [ProductDesign.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Product` in title) [ProductDesign.yaml:3]
- **Control Record:** ProductorServiceSpecification [ProductDesign.yaml:15]
- **Behavior Qualifiers (3):** FunctionalRequirements [ProductDesign.yaml:115], Testing [ProductDesign.yaml:248], Production [ProductDesign.yaml:327]
- **Operations (15):** Capture 1, Create 1, Exchange 2, Execute 2, Request 3, Retrieve 4, Update 2 [ProductDesign.yaml:12]
- **Schemas:** 31 total, 4 domain-specific, 27 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `ProductorServiceSpecification/Created`) [asyncapi:ProductDesign.yaml:9]

## Product Directory

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProductDirectory.yaml` (sha256 `a20f2b60af76…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProductDirectory.yaml`
- **Purpose (verbatim from spec):** This service domain maintains a comprehensive directory of the bank's products and services. It can be referenced to obtain product details used to support activities including product selection, sales and marketing, on-boarding, servicing and product fulfillment. [ProductDirectory.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Product` in title); Reference & Data Management (`Directory` in title); Securities, Trading & Markets (`market` in description); Channels & Servicing (`servicing` in description); Corporate Operations & Support (`service` in description) [ProductDirectory.yaml:3]
- **Control Record:** ProductDirectoryEntry [ProductDirectory.yaml:15]
- **Behavior Qualifiers (4):** Operations [ProductDirectory.yaml:91], SalesandMarketing [ProductDirectory.yaml:169], Servicing [ProductDirectory.yaml:271], Production [ProductDirectory.yaml:298]
- **Operations (16):** Register 5, Request 1, Retrieve 5, Update 5 [ProductDirectory.yaml:12]
- **Schemas:** 60 total, 16 domain-specific, 44 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `ProductDirectoryEntry/Created`) [asyncapi:ProductDirectory.yaml:12]

## Product Expert Sales Support

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProductExpertSalesSupport.yaml` (sha256 `2de14fe4fe82…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProductExpertSalesSupport.yaml`
- **Purpose (verbatim from spec):** Administer the availability and allocation of product specialists to support sales activity [ProductExpertSalesSupport.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Product` in title) [ProductExpertSalesSupport.yaml:3]
- **Control Record:** SalesSpecialistSupportAdministrativePlan [ProductExpertSalesSupport.yaml:15]
- **Behavior Qualifiers (1):** Assignment [ProductExpertSalesSupport.yaml:115]
- **Operations (10):** Capture 1, Create 2, Exchange 1, Request 2, Retrieve 2, Update 2 [ProductExpertSalesSupport.yaml:12]
- **Schemas:** 109 total, 2 domain-specific, 107 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `SalesSpecialistSupportAdministrativePlan/Created`) [asyncapi:ProductExpertSalesSupport.yaml:9]

## Product Inventory Distribution

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProductInventoryDistribution.yaml` (sha256 `ba529890a7c3…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProductInventoryDistribution.yaml`
- **Purpose (verbatim from spec):** Administer the provisioning and distribution of product inventory across the branch network and/or distribute direct to customers (e.g. mail) where appropriate [ProductInventoryDistribution.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Product` in title); Channels & Servicing (`branch` in description); Corporate Operations & Support (`network` in description) [ProductInventoryDistribution.yaml:3]
- **Control Record:** ProductInventoryDistributionAdministrativePlan [ProductInventoryDistribution.yaml:15]
- **Behavior Qualifiers (4):** Oversight [ProductInventoryDistribution.yaml:219], Distribution [ProductInventoryDistribution.yaml:246], Mailing [ProductInventoryDistribution.yaml:273], Provisioning [ProductInventoryDistribution.yaml:300]
- **Operations (24):** Capture 5, Control 1, Exchange 1, Grant 1, Initiate 5, Request 1, Retrieve 5, Update 5 [ProductInventoryDistribution.yaml:12]
- **Schemas:** 70 total, 7 domain-specific, 63 shared-across-≥10-specs
- **Event channels:** 12 (e.g. `ProductInventoryDistributionAdministrativePlan/Created`) [asyncapi:ProductInventoryDistribution.yaml:10]

## Product Inventory Item Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProductInventoryItemManagement.yaml` (sha256 `068df0e011fc…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProductInventoryItemManagement.yaml`
- **Purpose (verbatim from spec):** Maintain and distribute product inventory [ProductInventoryItemManagement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Product` in title) [ProductInventoryItemManagement.yaml:3]
- **Control Record:** ProductInventoryAllocation [ProductInventoryItemManagement.yaml:15]
- **Behavior Qualifiers (1):** Assignment [ProductInventoryItemManagement.yaml:91]
- **Operations (8):** Exchange 1, Provide 1, Request 2, Retrieve 2, Update 2 [ProductInventoryItemManagement.yaml:12]
- **Schemas:** 96 total, 4 domain-specific, 92 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `ProductInventoryAllocation/Created`) [asyncapi:ProductInventoryItemManagement.yaml:9]

## Product Matching

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProductMatching.yaml` (sha256 `29f506987410…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProductMatching.yaml`
- **Purpose (verbatim from spec):** Capability used to match eligible product and product combinations to a customer based on prevailing conditions such as customer type, product interest, solicitation/retention, campaign alignment [ProductMatching.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Product` in title) [ProductMatching.yaml:3]
- **Control Record:** ProducttoCustomerCombinationAssessment [ProductMatching.yaml:15]
- **Behavior Qualifiers (4):** BankandCampaignAlignment [ProductMatching.yaml:193], ProductEligibility [ProductMatching.yaml:219], ContextCriteria [ProductMatching.yaml:245], ProductTypeSelection [ProductMatching.yaml:271]
- **Operations (19):** Evaluate 5, Exchange 1, Execute 1, Grant 1, Request 1, Retrieve 5, Update 5 [ProductMatching.yaml:12]
- **Schemas:** 45 total, 6 domain-specific, 39 shared-across-≥10-specs
- **Event channels:** 12 (e.g. `ProducttoCustomerCombinationAssessment/Created`) [asyncapi:ProductMatching.yaml:11]

## Product Portfolio

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProductPortfolio.yaml` (sha256 `48ff5449ea1b…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProductPortfolio.yaml`
- **Purpose (verbatim from spec):** Maintain a portfolio of analytical views of the product portfolio to support product profitability and performance analysis [ProductPortfolio.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Portfolio` in title); Customer, Sales & Marketing (`Product` in title); Reference & Data Management (`analytic` in description) [ProductPortfolio.yaml:3]
- **Control Record:** ProductPortfolioAnalysis [ProductPortfolio.yaml:15]
- **Behavior Qualifiers (1):** PerformanceAnalysis [ProductPortfolio.yaml:115]
- **Operations (10):** Evaluate 2, Exchange 1, Execute 1, Request 2, Retrieve 2, Update 2 [ProductPortfolio.yaml:12]
- **Schemas:** 29 total, 3 domain-specific, 26 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `ProductPortfolioAnalysis/Created`) [asyncapi:ProductPortfolio.yaml:10]

## Product Quality Assurance

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProductQualityAssurance.yaml` (sha256 `6f8d2679955b…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProductQualityAssurance.yaml`
- **Purpose (verbatim from spec):** Maintain and execute a portfolio of product quality assurance tests and certifications that can be applied to evaluate any aspect of production activity for quality assurance [ProductQualityAssurance.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Product` in title); Securities, Trading & Markets (`portfolio` in description) [ProductQualityAssurance.yaml:3]
- **Control Record:** ProductandServiceAssessment [ProductQualityAssurance.yaml:15]
- **Behavior Qualifiers (4):** FunctionalConsistencyChecks [ProductQualityAssurance.yaml:193], ProcessingErrorandIntegrityChecks [ProductQualityAssurance.yaml:219], ResiliencyandPerformanceChecks [ProductQualityAssurance.yaml:245], UsabilityChecks [ProductQualityAssurance.yaml:271]
- **Operations (19):** Exchange 1, Execute 1, Grant 1, Initiate 5, Request 1, Retrieve 5, Update 5 [ProductQualityAssurance.yaml:12]
- **Schemas:** 45 total, 6 domain-specific, 39 shared-across-≥10-specs
- **Event channels:** 12 (e.g. `ProductandServiceAssessment/Created`) [asyncapi:ProductQualityAssurance.yaml:10]

## Product Sales Support

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProductSalesSupport.yaml` (sha256 `7864a9473d89…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProductSalesSupport.yaml`
- **Purpose (verbatim from spec):** This Service Domain administers customer access to product specialists [ProductSalesSupport.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Product` in title); Corporate Operations & Support (`Service` in description) [ProductSalesSupport.yaml:3]
- **Control Record:** ProductSalesSupportAdministrativePlan [ProductSalesSupport.yaml:15]
- **Behavior Qualifiers (2):** StaffAssignment [ProductSalesSupport.yaml:217], StaffAvailabilityTracking [ProductSalesSupport.yaml:271]
- **Operations (20):** Control 1, Create 1, Exchange 3, Grant 3, Notify 3, Request 3, Retrieve 3, Update 3 [ProductSalesSupport.yaml:12]
- **Schemas:** 67 total, 5 domain-specific, 62 shared-across-≥10-specs
- **Event channels:** 11 (e.g. `ProductSalesSupportAdministrativePlan/Created`) [asyncapi:ProductSalesSupport.yaml:9]

## Product Service Agency

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProductServiceAgency.yaml` (sha256 `2d9f2f43cbf0…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProductServiceAgency.yaml`
- **Purpose (verbatim from spec):** This Service Domain establishes and maintains contractual arrangements with product and service agencies [ProductServiceAgency.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Product` in title); Corporate Operations & Support (`Service` in title) [ProductServiceAgency.yaml:3]
- **Control Record:** ServiceProviderAgreement [ProductServiceAgency.yaml:15]
- **Behavior Qualifiers (3):** LegalTerm [ProductServiceAgency.yaml:191], PolicyTerm [ProductServiceAgency.yaml:243], RegulatoryTerm [ProductServiceAgency.yaml:269]
- **Operations (26):** Control 1, Evaluate 4, Exchange 4, Grant 1, Notify 4, Request 4, Retrieve 4, Update 4 [ProductServiceAgency.yaml:12]
- **Schemas:** 85 total, 5 domain-specific, 80 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `ServiceProviderAgreement/Created`) [asyncapi:ProductServiceAgency.yaml:10]

## Product Training

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProductTraining.yaml` (sha256 `f78b0eb682dc…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProductTraining.yaml`
- **Purpose (verbatim from spec):** Develop and provide product specific training across the workforce. This includes all media and training mechanisms (on-line, self taught, classroom etc.) [ProductTraining.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Product` in title); Corporate Operations & Support (`workforce` in description) [ProductTraining.yaml:3]
- **Control Record:** ProductTrainingProcedure [ProductTraining.yaml:15]
- **Behavior Qualifiers (4):** ContentDevelopment [ProductTraining.yaml:193], ServiceDelivery [ProductTraining.yaml:220], ServiceScheduling [ProductTraining.yaml:247], ServiceEvaluation [ProductTraining.yaml:301]
- **Operations (28):** Control 1, Exchange 5, Execute 3, Initiate 4, Request 5, Retrieve 5, Update 5 [ProductTraining.yaml:12]
- **Schemas:** 69 total, 7 domain-specific, 62 shared-across-≥10-specs
- **Event channels:** 12 (e.g. `ProductTrainingProcedure/Created`) [asyncapi:ProductTraining.yaml:10]

## Production Release

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProductionRelease.yaml` (sha256 `7d1bd97b285c…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProductionRelease.yaml`
- **Purpose (verbatim from spec):** Maintain and apply production release tests for new and updated systems [ProductionRelease.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Product` in title); Corporate Operations & Support (`system` in description) [ProductionRelease.yaml:3]
- **Control Record:** ProductionSystemAssessment [ProductionRelease.yaml:15]
- **Behavior Qualifiers (4):** FunctionalRisk [ProductionRelease.yaml:167], ProductionRisk [ProductionRelease.yaml:194], BusinessRisk [ProductionRelease.yaml:244], OperationalRisk [ProductionRelease.yaml:323]
- **Operations (14):** Evaluate 1, Exchange 5, Grant 1, Request 1, Retrieve 5, Update 1 [ProductionRelease.yaml:12]
- **Schemas:** 22 total, 5 domain-specific, 17 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `ProductionSystemAssessment/Created`) [asyncapi:ProductionRelease.yaml:9]

## Program Trading

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProgramTrading.yaml` (sha256 `6492ce4838bb…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProgramTrading.yaml`
- **Purpose (verbatim from spec):** This Service Domain supports a program trading capability where the trading decisions are made based on predefined/programmed rules and policies. Manual oversight and monitoring capabilities are supported as appropriate [ProgramTrading.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Trading` in title); Risk, Compliance & Fraud (`polic` in description); Corporate Operations & Support (`Service` in description) [ProgramTrading.yaml:3]
- **Control Record:** ProgramTradingOperatingSession [ProgramTrading.yaml:15]
- **Behavior Qualifiers (3):** ProgramTradeExecution [ProgramTrading.yaml:217], ProgramTradedPortfolioAlgorithm [ProgramTrading.yaml:271], ProgramTradedPortfolioMaintenance [ProgramTrading.yaml:298]
- **Operations (29):** Control 1, Exchange 4, Execute 4, Initiate 4, Notify 4, Request 4, Retrieve 4, Update 4 [ProgramTrading.yaml:12]
- **Schemas:** 35 total, 5 domain-specific, 30 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `ProgramTradingOperatingSession/Created`) [asyncapi:ProgramTrading.yaml:11]

## Project Finance

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProjectFinance.yaml` (sha256 `868e51df9a90…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProjectFinance.yaml`
- **Purpose (verbatim from spec):** This Service Domain fulfills project financing by which major (government) projects can attract privet sector financing [ProjectFinance.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`Project` in title) [ProjectFinance.yaml:3]
- **Control Record:** ProjectFinanceFacility [ProjectFinance.yaml:15]
- **Behavior Qualifiers (4):** Placement [ProjectFinance.yaml:167], Maintenance [ProjectFinance.yaml:218], Repayment [ProjectFinance.yaml:271], InstrumentDesign [ProjectFinance.yaml:298]
- **Operations (36):** Control 1, Exchange 5, Execute 5, Initiate 5, Notify 5, Request 5, Retrieve 5, Update 5 [ProjectFinance.yaml:12]
- **Schemas:** 126 total, 6 domain-specific, 120 shared-across-≥10-specs
- **Event channels:** 17 (e.g. `ProjectFinanceFacility/Created`) [asyncapi:ProjectFinance.yaml:10]

## Promotional Events

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/PromotionalEvents.yaml` (sha256 `34a0387575b4…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: PromotionalEvents.yaml`
- **Purpose (verbatim from spec):** Develop the plan for and oversee promotional event activity, including budget and resource management [PromotionalEvents.yaml:4]
- **Theme [derived-rule]:** primary Finance, Accounting & Treasury; all matches: Finance, Accounting & Treasury (`budget` in description) [PromotionalEvents.yaml:4]
- **Control Record:** PromotionalEventManagementPlan [PromotionalEvents.yaml:96]
- **Behavior Qualifiers (3):** MarketTracking [PromotionalEvents.yaml:15], ImpactAssessment [PromotionalEvents.yaml:42], Participation [PromotionalEvents.yaml:69]
- **Operations (18):** Create 3, Execute 2, Grant 1, Request 4, Retrieve 4, Update 4 [PromotionalEvents.yaml:12]
- **Schemas:** 44 total, 9 domain-specific, 35 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `PromotionalEventManagementPlan/Created`) [asyncapi:PromotionalEvents.yaml:9]

## Prospect Campaign Design

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProspectCampaignDesign.yaml` (sha256 `adc7eea11ec5…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProspectCampaignDesign.yaml`
- **Purpose (verbatim from spec):** Design and refine prospect campaign specifications based on their impact [ProspectCampaignDesign.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Prospect` in title) [ProspectCampaignDesign.yaml:3]
- **Control Record:** ProspectCampaignSpecification [ProspectCampaignDesign.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (8):** Capture 1, Control 1, Create 1, Exchange 1, Execute 1, Request 1, Retrieve 1, Update 1 [ProspectCampaignDesign.yaml:12]
- **Schemas:** 50 total, 7 domain-specific, 43 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `ProspectCampaignSpecification/Created`) [asyncapi:ProspectCampaignDesign.yaml:9]

## Prospect Campaign Execution

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProspectCampaignExecution.yaml` (sha256 `4a0093297aa8…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProspectCampaignExecution.yaml`
- **Purpose (verbatim from spec):** Execute a prospect campaign (version) and track and respond to impact [ProspectCampaignExecution.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Prospect` in title) [ProspectCampaignExecution.yaml:3]
- **Control Record:** ProspectCampaignProcedure [ProspectCampaignExecution.yaml:15]
- **Behavior Qualifiers (3):** Execution [ProspectCampaignExecution.yaml:193], CandidateSelection [ProspectCampaignExecution.yaml:272], AnalysisFeedback [ProspectCampaignExecution.yaml:377]
- **Operations (18):** Control 1, Exchange 2, Execute 1, Initiate 3, Request 3, Retrieve 4, Update 4 [ProspectCampaignExecution.yaml:12]
- **Schemas:** 39 total, 9 domain-specific, 30 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `ProspectCampaignProcedure/Created`) [asyncapi:ProspectCampaignExecution.yaml:9]

## Prospect Campaign Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ProspectCampaignManagement.yaml` (sha256 `bef1da05f0f1…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ProspectCampaignManagement.yaml`
- **Purpose (verbatim from spec):** Assess the coverage and impact of external/prospect campaigns and redirect campaign development and execution activity accordingly [ProspectCampaignManagement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Prospect` in title) [ProspectCampaignManagement.yaml:3]
- **Control Record:** ProspectCampaignPortfolioManagementPlan [ProspectCampaignManagement.yaml:15]
- **Behavior Qualifiers (3):** MarketTracking [ProspectCampaignManagement.yaml:41], CampaignDirection [ProspectCampaignManagement.yaml:68], PerformanceAssessment [ProspectCampaignManagement.yaml:198]
- **Operations (18):** Create 3, Execute 2, Grant 1, Request 4, Retrieve 4, Update 4 [ProspectCampaignManagement.yaml:12]
- **Schemas:** 63 total, 10 domain-specific, 53 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `ProspectCampaignPortfolioManagementPlan/Created`) [asyncapi:ProspectCampaignManagement.yaml:10]

## Public Offering

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/PublicOffering.yaml` (sha256 `d64e9e8d6e49…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: PublicOffering.yaml`
- **Purpose (verbatim from spec):** This Service Domain supports a broad range of complex financial, accounting and regulatory actions involved in providing advice and practical support to companies going public and/or raising additional capital through the issuance of publicly traded securities [PublicOffering.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`securit` in description); Risk, Compliance & Fraud (`regulat` in description); Deposits & Accounts (`account` in description); Finance, Accounting & Treasury (`financial` in description); Corporate Operations & Support (`Service` in description) [PublicOffering.yaml:4]
- **Control Record:** PublicOfferingFacility [PublicOffering.yaml:15]
- **Behavior Qualifiers (6):** Compliance [PublicOffering.yaml:217], ItemRegistration [PublicOffering.yaml:244], Underwriting [PublicOffering.yaml:271], InstrumentDesign [PublicOffering.yaml:298], Prospectus [PublicOffering.yaml:325], Placement [PublicOffering.yaml:460]
- **Operations (50):** Control 1, Exchange 7, Execute 7, Initiate 7, Notify 7, Request 7, Retrieve 7, Update 7 [PublicOffering.yaml:12]
- **Schemas:** 128 total, 8 domain-specific, 120 shared-across-≥10-specs
- **Event channels:** 23 (e.g. `PublicOfferingFacility/Created`) [asyncapi:PublicOffering.yaml:12]

## Public Reference Data Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/PublicReferenceDataManagement.yaml` (sha256 `ca08e7449782…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: PublicReferenceDataManagement.yaml`
- **Purpose (verbatim from spec):** Provide structured access to standard 'global' reference data and definitions associated with market activity such as currency, country and segment identifiers. [PublicReferenceDataManagement.yaml:4]
- **Theme [derived-rule]:** primary Reference & Data Management; all matches: Reference & Data Management (`Reference` in title); Securities, Trading & Markets (`market` in description) [PublicReferenceDataManagement.yaml:3]
- **Control Record:** GlobalStandardSpecification [PublicReferenceDataManagement.yaml:15]
- **Behavior Qualifiers (1):** GlobalReferenceData [PublicReferenceDataManagement.yaml:193]
- **Operations (9):** Capture 1, Control 1, Exchange 1, Initiate 2, Request 1, Retrieve 2, Update 1 [PublicReferenceDataManagement.yaml:12]
- **Schemas:** 23 total, 3 domain-specific, 20 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `GlobalStandardSpecification/Created`) [asyncapi:PublicReferenceDataManagement.yaml:10]

## Quote Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/QuoteManagement.yaml` (sha256 `df4c7fe9e895…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: QuoteManagement.yaml`
- **Purpose (verbatim from spec):** This service domain handles the procedure used by traders to obtain and selecting quotes from market makers [QuoteManagement.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`trader` in description); Corporate Operations & Support (`service` in description) [QuoteManagement.yaml:4]
- **Control Record:** QuotationProcedure [QuoteManagement.yaml:15]
- **Behavior Qualifiers (2):** MarketQuoteSelection [QuoteManagement.yaml:217], MarketQuoteRequest [QuoteManagement.yaml:244]
- **Operations (22):** Control 1, Exchange 3, Execute 3, Initiate 3, Notify 3, Request 3, Retrieve 3, Update 3 [QuoteManagement.yaml:12]
- **Schemas:** 75 total, 4 domain-specific, 71 shared-across-≥10-specs
- **Event channels:** 11 (e.g. `QuotationProcedure/Created`) [asyncapi:QuoteManagement.yaml:10]

## Regulatory And Legal Authority

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/RegulatoryAndLegalAuthority.yaml` (sha256 `ce8568784f8e…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: RegulatoryAndLegalAuthority.yaml`
- **Purpose (verbatim from spec):** Maintain effective relations with regulators, accounting and government agencies. Oversee interactions and reporting as necessary [RegulatoryAndLegalAuthority.yaml:4]
- **Theme [derived-rule]:** primary Risk, Compliance & Fraud; all matches: Risk, Compliance & Fraud (`Regulat` in title); Deposits & Accounts (`account` in description); Finance, Accounting & Treasury (`accounting` in description); Reference & Data Management (`report` in description) [RegulatoryAndLegalAuthority.yaml:3]
- **Control Record:** RegulatoryAndLegalAuthorityRelationshipManagementPlan [RegulatoryAndLegalAuthority.yaml:15]
- **Behavior Qualifiers (4):** RepresentBankInterests [RegulatoryAndLegalAuthority.yaml:41], Troubleshooting [RegulatoryAndLegalAuthority.yaml:194], MaintainRelations [RegulatoryAndLegalAuthority.yaml:221], EstablishRelations [RegulatoryAndLegalAuthority.yaml:298]
- **Operations (25):** Capture 2, Control 1, Exchange 1, Grant 1, Initiate 5, Request 5, Retrieve 5, Update 5 [RegulatoryAndLegalAuthority.yaml:12]
- **Schemas:** 67 total, 10 domain-specific, 57 shared-across-≥10-specs
- **Event channels:** 12 (e.g. `RegulatoryAndLegalAuthorityRelationshipManagementPlan/Created`) [asyncapi:RegulatoryAndLegalAuthority.yaml:10]

## Regulatory Compliance

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/RegulatoryCompliance.yaml` (sha256 `457f65073033…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: RegulatoryCompliance.yaml`
- **Purpose (verbatim from spec):** This service domain provides a service to interpret regulatory requirements, provide guidance and define and implement a portfolio of regulatory compliance tests across all appropriate bank activities [RegulatoryCompliance.yaml:4]
- **Theme [derived-rule]:** primary Risk, Compliance & Fraud; all matches: Risk, Compliance & Fraud (`Regulat` in title); Securities, Trading & Markets (`portfolio` in description); Corporate Operations & Support (`service` in description) [RegulatoryCompliance.yaml:3]
- **Control Record:** RegulatoryComplianceAssessment [RegulatoryCompliance.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (5):** Capture 1, Evaluate 1, Request 1, Retrieve 1, Update 1 [RegulatoryCompliance.yaml:12]
- **Schemas:** 42 total, 4 domain-specific, 38 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `RegulatoryComplianceAssessment/Created`) [asyncapi:RegulatoryCompliance.yaml:11]

## Regulatory Reporting

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/RegulatoryReporting.yaml` (sha256 `ab66f9c905a6…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: RegulatoryReporting.yaml`
- **Purpose (verbatim from spec):** This service domain administers and orchestrates the tasks required to meet the bank's regulatory reporting obligations [RegulatoryReporting.yaml:4]
- **Theme [derived-rule]:** primary Risk, Compliance & Fraud; all matches: Risk, Compliance & Fraud (`Regulat` in title); Reference & Data Management (`Report` in title); Corporate Operations & Support (`service` in description) [RegulatoryReporting.yaml:3]
- **Control Record:** RegulatoryComplianceAdministrativePlan [RegulatoryReporting.yaml:15]
- **Behavior Qualifiers (3):** Consolidation [RegulatoryReporting.yaml:115], Authoring [RegulatoryReporting.yaml:140], Enquiries [RegulatoryReporting.yaml:221]
- **Operations (13):** Capture 2, Create 1, Exchange 2, Request 1, Retrieve 4, Update 3 [RegulatoryReporting.yaml:12]
- **Schemas:** 52 total, 6 domain-specific, 46 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `RegulatoryComplianceAdministrativePlan/Created`) [asyncapi:RegulatoryReporting.yaml:10]

## Reward Points Account

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/RewardPointsAccount.yaml` (sha256 `a229aec2a66a…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: RewardPointsAccount.yaml`
- **Purpose (verbatim from spec):** Administer the booking and remittance of rewards points [RewardPointsAccount.yaml:4]
- **Theme [derived-rule]:** primary Deposits & Accounts; all matches: Deposits & Accounts (`Account` in title); Payments & Settlement (`remittance` in description) [RewardPointsAccount.yaml:3]
- **Control Record:** RewardPointsLog [RewardPointsAccount.yaml:15]
- **Behavior Qualifiers (2):** Capture [RewardPointsAccount.yaml:219], Expiration [RewardPointsAccount.yaml:246]
- **Operations (16):** Capture 3, Control 1, Exchange 1, Grant 1, Initiate 3, Request 1, Retrieve 3, Update 3 [RewardPointsAccount.yaml:12]
- **Schemas:** 46 total, 5 domain-specific, 41 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `RewardPointsLog/Created`) [asyncapi:RewardPointsAccount.yaml:9]

## Reward Points Awards And Redemption

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/RewardPointsAwardsAndRedemption.yaml` (sha256 `894479ceb326…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: RewardPointsAwardsAndRedemption.yaml`
- **Purpose (verbatim from spec):** Handle the allocation and redemption of rewards points for customer transaction activity [RewardPointsAwardsAndRedemption.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`customer` in description) [RewardPointsAwardsAndRedemption.yaml:4]
- **Control Record:** RewardPointsTransaction [RewardPointsAwardsAndRedemption.yaml:15]
- **Behavior Qualifiers (2):** Award [RewardPointsAwardsAndRedemption.yaml:167], Redemption [RewardPointsAwardsAndRedemption.yaml:194]
- **Operations (14):** Exchange 3, Execute 1, Initiate 3, Request 1, Retrieve 3, Update 3 [RewardPointsAwardsAndRedemption.yaml:12]
- **Schemas:** 119 total, 5 domain-specific, 114 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `RewardPointsTransaction/Created`) [asyncapi:RewardPointsAwardsAndRedemption.yaml:9]

## Rewards Delivery

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/RewardsDelivery.yaml` (sha256 `6af0c70a2eb2…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: RewardsDelivery.yaml`
- **Purpose (verbatim from spec):** The service domain orchestrates the entire end-to-end process for delivering a redeemed reward. [RewardsDelivery.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`service` in description) [RewardsDelivery.yaml:4]
- **Behavior Qualifiers:** none
- **Operations:** none defined (the OpenAPI `paths` section is empty or absent)
- **Schemas:** 2 total, 1 domain-specific, 1 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `RewardsDeliveryProcedure/Created`) [asyncapi:RewardsDelivery.yaml:10]

## Rewards Inventory

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/RewardsInventory.yaml` (sha256 `a13f626f28a6…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: RewardsInventory.yaml`
- **Purpose (verbatim from spec):** The service domain handles the allocation of rewards from available inventory. [RewardsInventory.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`service` in description) [RewardsInventory.yaml:4]
- **Behavior Qualifiers:** none
- **Operations:** none defined (the OpenAPI `paths` section is empty or absent)
- **Schemas:** 2 total, 1 domain-specific, 1 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `RewardsInventoryAllocation/Created`) [asyncapi:RewardsInventory.yaml:9]

## Rewards Menu

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/RewardsMenu.yaml` (sha256 `09ba7625dbb4…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: RewardsMenu.yaml`
- **Purpose (verbatim from spec):** The service domain presents a set of eligible rewards a customer can select from. [RewardsMenu.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`customer` in description); Corporate Operations & Support (`service` in description) [RewardsMenu.yaml:4]
- **Behavior Qualifiers:** none
- **Operations:** none defined (the OpenAPI `paths` section is empty or absent)
- **Schemas:** 2 total, 1 domain-specific, 1 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `RewardsOptionDirectoryEntry/Created`) [asyncapi:RewardsMenu.yaml:9]

## Sales Product

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/SalesProduct.yaml` (sha256 `d96f813c01c6…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: SalesProduct.yaml`
- **Purpose (verbatim from spec):** A representation of a product as sold to a customer, covering the operational fulfillment requirements [SalesProduct.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Sales` in title) [SalesProduct.yaml:3]
- **Control Record:** ProductandServiceAgreement [SalesProduct.yaml:15]
- **Behavior Qualifiers (1):** OperationalTerm [SalesProduct.yaml:65]
- **Operations (9):** Control 1, Evaluate 2, Exchange 1, Grant 1, Retrieve 2, Update 2 [SalesProduct.yaml:12]
- **Schemas:** 75 total, 5 domain-specific, 70 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `ProductandServiceAgreement/Created`) [asyncapi:SalesProduct.yaml:10]

## Sales Product Agreement

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/SalesProductAgreement.yaml` (sha256 `b21600fde4ae…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: SalesProductAgreement.yaml`
- **Purpose (verbatim from spec):** This service domain maintains a structured legal agreement defining the contractual terms and conditions for an in-force product for a customer. It is subordinate to the customer's master agreement that is maintained by the Customer Agreement service domain [SalesProductAgreement.yaml:4]
- **Theme [derived-rule]:** primary Customer, Sales & Marketing; all matches: Customer, Sales & Marketing (`Sales` in title); Risk, Compliance & Fraud (`legal` in description); Corporate Operations & Support (`service` in description) [SalesProductAgreement.yaml:3]
- **Control Record:** SalesProductAgreement [SalesProductAgreement.yaml:15]
- **Behavior Qualifiers (3):** LegalTerm [SalesProductAgreement.yaml:193], RegulatoryTerm [SalesProductAgreement.yaml:271], PolicyTerm [SalesProductAgreement.yaml:349]
- **Operations (16):** Control 1, Evaluate 4, Exchange 1, Grant 1, Request 1, Retrieve 4, Update 4 [SalesProductAgreement.yaml:12]
- **Schemas:** 52 total, 12 domain-specific, 40 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `SalesProductAgreement/Created`) [asyncapi:SalesProductAgreement.yaml:12]
- **Other domains named in this purpose text:** Customer Agreement [SalesProductAgreement.yaml:4]

## Savings Account

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/SavingsAccount.yaml` (sha256 `897c439dd0b4…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: SavingsAccount.yaml`
- **Purpose (verbatim from spec):** This service domain orchestrates a consumer savings account. The typical range of services and fees covers payments from and scheduled and ad-hoc deposits to the account, standing orders, sweeps, and liens. [SavingsAccount.yaml:4]
- **Theme [derived-rule]:** primary Deposits & Accounts; all matches: Deposits & Accounts (`Saving` in title); Payments & Settlement (`payment` in description); Finance, Accounting & Treasury (`fees` in description); Corporate Operations & Support (`service` in description) [SavingsAccount.yaml:3]
- **Control Record:** SavingsAccountFacility [SavingsAccount.yaml:15]
- **Behavior Qualifiers (9):** Charge [SavingsAccount.yaml:115], Interest [SavingsAccount.yaml:142], Sweep [SavingsAccount.yaml:192], DebitandCredit [SavingsAccount.yaml:323], Payment [SavingsAccount.yaml:401], IssuedDevice [SavingsAccount.yaml:560], Booking [SavingsAccount.yaml:667], AmountBlock [SavingsAccount.yaml:719], Deposit [SavingsAccount.yaml:797]
- **Operations (34):** Control 1, Exchange 1, Execute 7, Initiate 8, Retrieve 9, Update 8 [SavingsAccount.yaml:12]
- **Schemas:** 251 total, 38 domain-specific, 213 shared-across-≥10-specs
- **Event channels:** 20 (e.g. `SavingsAccountFacility/Created`) [asyncapi:SavingsAccount.yaml:11]

## Securities Fails Processing

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/SecuritiesFailsProcessing.yaml` (sha256 `600d1ff5ae3c…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: SecuritiesFailsProcessing.yaml`
- **Purpose (verbatim from spec):** This Service Domain handles the resolution of clerical and processing errors that lead to failures in the securities trade clearing and settlement processes [SecuritiesFailsProcessing.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Securit` in title); Payments & Settlement (`clearing` in description); Customer, Sales & Marketing (`lead` in description); Corporate Operations & Support (`Service` in description) [SecuritiesFailsProcessing.yaml:3]
- **Control Record:** SecurityTradingFailsProcedure [SecuritiesFailsProcessing.yaml:15]
- **Behavior Qualifiers (2):** SecuritiesFailAnalysis [SecuritiesFailsProcessing.yaml:217], SecuritiesFailDetermination [SecuritiesFailsProcessing.yaml:244]
- **Operations (22):** Control 1, Exchange 3, Execute 3, Initiate 3, Notify 3, Request 3, Retrieve 3, Update 3 [SecuritiesFailsProcessing.yaml:12]
- **Schemas:** 75 total, 4 domain-specific, 71 shared-across-≥10-specs
- **Event channels:** 11 (e.g. `SecurityTradingFailsProcedure/Created`) [asyncapi:SecuritiesFailsProcessing.yaml:10]
- **Other domains named in this purpose text:** Trade Clearing [SecuritiesFailsProcessing.yaml:4]

## Securities Position Keeping

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/SecuritiesPositionKeeping.yaml` (sha256 `4a646189d982…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: SecuritiesPositionKeeping.yaml`
- **Purpose (verbatim from spec):** This service domain maintains a securities transaction log to support securities investment activity [SecuritiesPositionKeeping.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Securit` in title); Corporate Operations & Support (`service` in description) [SecuritiesPositionKeeping.yaml:3]
- **Control Record:** SecuritiesPositionLog [SecuritiesPositionKeeping.yaml:15]
- **Behavior Qualifiers (1):** SecuritiesTransactionCapture [SecuritiesPositionKeeping.yaml:115]
- **Operations (7):** Capture 1, Control 1, Initiate 1, Retrieve 2, Update 2 [SecuritiesPositionKeeping.yaml:12]
- **Schemas:** 30 total, 2 domain-specific, 28 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `SecuritiesPositionLog/Created`) [asyncapi:SecuritiesPositionKeeping.yaml:10]

## Segment Direction

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/SegmentDirection.yaml` (sha256 `8b2ffe17e789…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: SegmentDirection.yaml`
- **Purpose (verbatim from spec):** Define market segments and develop and assess performance against the segment plan's performance goals [SegmentDirection.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`market` in description) [SegmentDirection.yaml:4]
- **Control Record:** SegmentStrategy [SegmentDirection.yaml:15]
- **Behavior Qualifiers (1):** Initiative [SegmentDirection.yaml:193]
- **Operations (13):** Capture 2, Create 2, Exchange 2, Grant 1, Request 2, Retrieve 2, Update 2 [SegmentDirection.yaml:12]
- **Schemas:** 50 total, 5 domain-specific, 45 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `SegmentStrategy/Created`) [asyncapi:SegmentDirection.yaml:9]

## Service Directory

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ServiceDirectory.yaml` (sha256 `318b88050eab…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ServiceDirectory.yaml`
- **Purpose (verbatim from spec):** This Service Domain presents a structured set of services that the customer can select from [ServiceDirectory.yaml:4]
- **Theme [derived-rule]:** primary Reference & Data Management; all matches: Reference & Data Management (`Directory` in title); Corporate Operations & Support (`Service` in title); Customer, Sales & Marketing (`customer` in description) [ServiceDirectory.yaml:3]
- **Control Record:** ServiceDirectoryEntry [ServiceDirectory.yaml:15]
- **Behavior Qualifiers (6):** AccessControlServicing [ServiceDirectory.yaml:191], ArrangementServicing [ServiceDirectory.yaml:218], ProductAccessServicing [ServiceDirectory.yaml:245], RelationshipServicing [ServiceDirectory.yaml:272], ServiceDeliveryServicing [ServiceDirectory.yaml:299], SalesServicing [ServiceDirectory.yaml:326]
- **Operations (43):** Control 1, Execute 7, Notify 7, Register 7, Request 7, Retrieve 7, Update 7 [ServiceDirectory.yaml:12]
- **Schemas:** 32 total, 9 domain-specific, 23 shared-across-≥10-specs
- **Event channels:** 23 (e.g. `ServiceDirectoryEntry/Created`) [asyncapi:ServiceDirectory.yaml:9]

## Service Provider Operations

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ServiceProviderOperations.yaml` (sha256 `895c5e4f150a…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ServiceProviderOperations.yaml`
- **Purpose (verbatim from spec):** This Service Domain handles the range of operational actions used in production interactions with an external service provider. [ServiceProviderOperations.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`Service` in title); Customer, Sales & Marketing (`product` in description) [ServiceProviderOperations.yaml:3]
- **Control Record:** ServiceProviderRegistrationOperatingSession [ServiceProviderOperations.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (1):** Retrieve 1 [ServiceProviderOperations.yaml:12]
- **Schemas:** 38 total, 13 domain-specific, 25 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `ServiceProviderRegistrationOperatingSession/Created`) [asyncapi:ServiceProviderOperations.yaml:10]

## Servicing Activity Analysis

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ServicingActivityAnalysis.yaml` (sha256 `754d21a7078e…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ServicingActivityAnalysis.yaml`
- **Purpose (verbatim from spec):** This service domain analyzes servicing activity to support continual service improvement [ServicingActivityAnalysis.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Servicing` in title); Corporate Operations & Support (`service` in description) [ServicingActivityAnalysis.yaml:3]
- **Control Record:** ServicingRootCauseAnalysis [ServicingActivityAnalysis.yaml:15]
- **Behavior Qualifiers (1):** RootCauseAlgorithm [ServicingActivityAnalysis.yaml:141]
- **Operations (8):** Execute 1, Initiate 2, Request 2, Retrieve 2, Update 1 [ServicingActivityAnalysis.yaml:12]
- **Schemas:** 17 total, 2 domain-specific, 15 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `ServicingRootCauseAnalysis/Created`) [asyncapi:ServicingActivityAnalysis.yaml:9]

## Servicing Event History

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ServicingEventHistory.yaml` (sha256 `0f84fa12e847…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ServicingEventHistory.yaml`
- **Purpose (verbatim from spec):** This service domain captures, classifies and stores servicing activity and events to support root cause analysis [ServicingEventHistory.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Servicing` in title); Corporate Operations & Support (`service` in description) [ServicingEventHistory.yaml:3]
- **Control Record:** ServicingEventLog [ServicingEventHistory.yaml:15]
- **Behavior Qualifiers (4):** Assignment [ServicingEventHistory.yaml:39], Session [ServicingEventHistory.yaml:169], Issue [ServicingEventHistory.yaml:273], ServicingFacility [ServicingEventHistory.yaml:352]
- **Operations (16):** Capture 4, Control 1, Initiate 1, Retrieve 5, Update 5 [ServicingEventHistory.yaml:12]
- **Schemas:** 41 total, 4 domain-specific, 37 shared-across-≥10-specs
- **Event channels:** 10 (e.g. `ServicingEventLog/Created`) [asyncapi:ServicingEventHistory.yaml:10]

## Servicing Issue

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ServicingIssue.yaml` (sha256 `517905272ed5…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ServicingIssue.yaml`
- **Purpose (verbatim from spec):** This Service Domain handles production customer servicing issues detected in the customer servicing environment [ServicingIssue.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Servicing` in title); Customer, Sales & Marketing (`product` in description); Corporate Operations & Support (`Service` in description) [ServicingIssue.yaml:3]
- **Control Record:** ServicingIssueProcedure [ServicingIssue.yaml:15]
- **Behavior Qualifiers (3):** ProductionIssueAnalysis [ServicingIssue.yaml:217], ProductionIssueDetermination [ServicingIssue.yaml:244], ProductionIssueResolution [ServicingIssue.yaml:271]
- **Operations (29):** Control 1, Exchange 4, Execute 4, Initiate 4, Notify 4, Request 4, Retrieve 4, Update 4 [ServicingIssue.yaml:12]
- **Schemas:** 76 total, 5 domain-specific, 71 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `ServicingIssueProcedure/Created`) [asyncapi:ServicingIssue.yaml:10]

## Servicing Mandate

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ServicingMandate.yaml` (sha256 `3e61d650ffac…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ServicingMandate.yaml`
- **Purpose (verbatim from spec):** This service domain maintains the allowed customer servicing arrangements for a service provider covering general access to the bank's products and services and optionally customer specific arrangements [ServicingMandate.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Servicing` in title); Customer, Sales & Marketing (`customer` in description); Corporate Operations & Support (`service` in description) [ServicingMandate.yaml:3]
- **Control Record:** ServicingMandateAgreement [ServicingMandate.yaml:15]
- **Behavior Qualifiers (1):** CustomerMandate [ServicingMandate.yaml:193]
- **Operations (13):** Control 2, Evaluate 2, Exchange 2, Grant 2, Request 1, Retrieve 2, Update 2 [ServicingMandate.yaml:12]
- **Schemas:** 59 total, 14 domain-specific, 45 shared-across-≥10-specs
- **Event channels:** 4 (e.g. `ServicingMandateAgreement/Created`) [asyncapi:ServicingMandate.yaml:11]

## Servicing Order

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/ServicingOrder.yaml` (sha256 `64173e3c1c82…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: ServicingOrder.yaml`
- **Purpose (verbatim from spec):** This service domain handles the processing of a customer servicing request as a predefined procedure. A range of standard servicing requests can be supported. The process can include a check of permissions when the request is made by a third party/service provider [ServicingOrder.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Servicing` in title); Customer, Sales & Marketing (`customer` in description); Corporate Operations & Support (`service` in description) [ServicingOrder.yaml:3]
- **Control Record:** ServicingOrderProcedure [ServicingOrder.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (7):** Control 1, Exchange 1, Execute 1, Initiate 1, Request 1, Retrieve 1, Update 1 [ServicingOrder.yaml:12]
- **Schemas:** 25 total, 1 domain-specific, 24 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `ServicingOrderProcedure/Created`) [asyncapi:ServicingOrder.yaml:12]

## Session Dialogue

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/SessionDialogue.yaml` (sha256 `e88c65cf7a3d…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: SessionDialogue.yaml`
- **Purpose (verbatim from spec):** This service domain handles/structures the customer narrative during an interactive session. It consolidates and presents pertinent customer information and provides servicing guidelines with standard dialogue/scripting as appropriate. It can include the capability to provoke questions to capture k… [SessionDialogue.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Session` in title); Customer, Sales & Marketing (`customer` in description); Reference & Data Management (`information` in description); Corporate Operations & Support (`service` in description) [SessionDialogue.yaml:3]
- **Control Record:** CustomerContactSessionProcedure [SessionDialogue.yaml:15]
- **Behavior Qualifiers (9):** Query [SessionDialogue.yaml:193], Authentication [SessionDialogue.yaml:271], Sales [SessionDialogue.yaml:296], Offer [SessionDialogue.yaml:401], ProductorService [SessionDialogue.yaml:479], Case [SessionDialogue.yaml:557], Order [SessionDialogue.yaml:635], Intelligence [SessionDialogue.yaml:713], History [SessionDialogue.yaml:791]
- **Operations (35):** Control 1, Exchange 3, Execute 2, Initiate 8, Request 1, Retrieve 10, Update 10 [SessionDialogue.yaml:12]
- **Schemas:** 43 total, 15 domain-specific, 28 shared-across-≥10-specs
- **Event channels:** 20 (e.g. `CustomerContactSessionProcedure/Created`) [asyncapi:SessionDialogue.yaml:16]

## Special Pricing Conditions

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/SpecialPricingConditions.yaml` (sha256 `7a36afe82dec…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: SpecialPricingConditions.yaml`
- **Purpose (verbatim from spec):** Maintain a pricing list or conditions (with ranges and optional terms) categorized by various dimensions to impose exceptional product pricing conditions that override standard pricing terms (for special events/situations) [SpecialPricingConditions.yaml:4]
- **Theme [derived-rule]:** primary Reference & Data Management; all matches: Reference & Data Management (`Pricing` in title); Customer, Sales & Marketing (`product` in description) [SpecialPricingConditions.yaml:3]
- **Control Record:** SpecialPricingConditionsDirectoryEntry [SpecialPricingConditions.yaml:15]
- **Behavior Qualifiers (1):** PricingTerms [SpecialPricingConditions.yaml:193]
- **Operations (10):** Control 1, Exchange 1, Execute 1, Initiate 2, Request 1, Retrieve 2, Update 2 [SpecialPricingConditions.yaml:12]
- **Schemas:** 32 total, 3 domain-specific, 29 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `SpecialPricingConditionsDirectoryEntry/Created`) [asyncapi:SpecialPricingConditions.yaml:11]

## Standing Order

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/StandingOrder.yaml` (sha256 `76f6d54c24f6…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: StandingOrder.yaml`
- **Purpose (verbatim from spec):** Customers can issue standing orders to the bank. In most cases this is for the execution of a periodical payment, but there are other standing instructions like, sweeping balances at end of month, topping off excess funds for a current account, etc. [StandingOrder.yaml:4]
- **Theme [derived-rule]:** primary Payments & Settlement; all matches: Payments & Settlement (`payment` in description); Securities, Trading & Markets (`funds` in description); Deposits & Accounts (`balance` in description); Customer, Sales & Marketing (`Customer` in description) [StandingOrder.yaml:4]
- **Control Record:** StandingOrderFacility [StandingOrder.yaml:15]
- **Behavior Qualifiers (1):** StandingOrderPayment [StandingOrder.yaml:193]
- **Operations (11):** Control 1, Exchange 2, Execute 1, Initiate 2, Request 1, Retrieve 2, Update 2 [StandingOrder.yaml:12]
- **Schemas:** 110 total, 4 domain-specific, 106 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `StandingOrderFacility/Created`) [asyncapi:StandingOrder.yaml:12]
- **Other domains named in this purpose text:** Current Account [StandingOrder.yaml:4]

## Stock Lending and Repos

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/StockLendingandRepos.yaml` (sha256 `e6bfbf426340…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: StockLendingandRepos.yaml`
- **Purpose (verbatim from spec):** This Service Domain supports the bank offering tri-party repo transactions made between its customers to support their short term capital management requirements [StockLendingandRepos.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Lend` in title); Customer, Sales & Marketing (`party` in description); Finance, Accounting & Treasury (`capital` in description); Corporate Operations & Support (`Service` in description) [StockLendingandRepos.yaml:3]
- **Control Record:** RepoTransaction [StockLendingandRepos.yaml:15]
- **Behavior Qualifiers (3):** RepoTransactionCashTransfer [StockLendingandRepos.yaml:217], RepoTransactionInitiation [StockLendingandRepos.yaml:244], RepoTransactionSecurityTransfer [StockLendingandRepos.yaml:271]
- **Operations (29):** Control 1, Exchange 4, Execute 4, Initiate 4, Notify 4, Request 4, Retrieve 4, Update 4 [StockLendingandRepos.yaml:12]
- **Schemas:** 76 total, 11 domain-specific, 65 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `RepoTransaction/Created`) [asyncapi:StockLendingandRepos.yaml:10]

## Sub Custodian Agreement

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/SubCustodianAgreement.yaml` (sha256 `d4449c5d7729…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: SubCustodianAgreement.yaml`
- **Purpose (verbatim from spec):** This Service Domain establishes and maintains the terms governing sub custodian relationship [SubCustodianAgreement.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Custod` in title); Customer, Sales & Marketing (`relationship` in description); Corporate Operations & Support (`Service` in description) [SubCustodianAgreement.yaml:3]
- **Control Record:** SubCustodianAgreement [SubCustodianAgreement.yaml:15]
- **Behavior Qualifiers (3):** LegalTerm [SubCustodianAgreement.yaml:191], PolicyTerm [SubCustodianAgreement.yaml:243], RegulatoryTerm [SubCustodianAgreement.yaml:296]
- **Operations (26):** Control 1, Evaluate 4, Exchange 4, Grant 1, Notify 4, Request 4, Retrieve 4, Update 4 [SubCustodianAgreement.yaml:12]
- **Schemas:** 85 total, 5 domain-specific, 80 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `SubCustodianAgreement/Created`) [asyncapi:SubCustodianAgreement.yaml:9]

## Suitability Checking

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/SuitabilityChecking.yaml` (sha256 `db00864da72b…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: SuitabilityChecking.yaml`
- **Purpose (verbatim from spec):** Confirm that all involved counterparties are suitable for a proposed market trade. [SuitabilityChecking.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`market` in description) [SuitabilityChecking.yaml:4]
- **Control Record:** SuitabilityAssessment [SuitabilityChecking.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (6):** Evaluate 1, Exchange 1, Grant 1, Request 1, Retrieve 1, Update 1 [SuitabilityChecking.yaml:12]
- **Schemas:** 45 total, 2 domain-specific, 43 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `SuitabilityAssessment/Created`) [asyncapi:SuitabilityChecking.yaml:9]

## Syndicate Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/SyndicateManagement.yaml` (sha256 `b067f5baab39…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: SyndicateManagement.yaml`
- **Purpose (verbatim from spec):** This Service Domain manages syndicate membership and compliance [SyndicateManagement.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Syndicat` in title); Risk, Compliance & Fraud (`complian` in description); Corporate Operations & Support (`Service` in description) [SyndicateManagement.yaml:3]
- **Control Record:** SyndicateMembership [SyndicateManagement.yaml:15]
- **Behavior Qualifiers (2):** SyndicateComplianceClauses [SyndicateManagement.yaml:191], SyndicateEligibilityClauses [SyndicateManagement.yaml:216]
- **Operations (13):** Control 1, Grant 1, Notify 3, Register 1, Request 1, Retrieve 3, Update 3 [SyndicateManagement.yaml:12]
- **Schemas:** 62 total, 5 domain-specific, 57 shared-across-≥10-specs
- **Event channels:** 11 (e.g. `SyndicateMembership/Created`) [asyncapi:SyndicateManagement.yaml:9]

## Syndicated Loan

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/SyndicatedLoan.yaml` (sha256 `0009e8b69971…`, version 14.0.0); bundle: `oas3_yamls_part5.md` under `# FILE: SyndicatedLoan.yaml`
- **Purpose (verbatim from spec):** Handle the processing of syndicated loans with the bank playing the lead coordination role with other syndicate bank members. Note some initial preparation may have been made through prior customer offer processing. [SyndicatedLoan.yaml:4]
- **Theme [derived-rule]:** primary Lending & Credit; all matches: Lending & Credit (`Syndicat` in title); Customer, Sales & Marketing (`lead` in description) [SyndicatedLoan.yaml:3]
- **Control Record:** SyndicatedLoanFacility [SyndicatedLoan.yaml:15]
- **Behavior Qualifiers (4):** Fulfillment [SyndicatedLoan.yaml:193], Origination [SyndicatedLoan.yaml:220], Syndicate [SyndicatedLoan.yaml:247], InstrumentDesign [SyndicatedLoan.yaml:274]
- **Operations (24):** Control 1, Exchange 5, Execute 1, Initiate 2, Request 5, Retrieve 5, Update 5 [SyndicatedLoan.yaml:12]
- **Schemas:** 58 total, 8 domain-specific, 50 shared-across-≥10-specs
- **Event channels:** 12 (e.g. `SyndicatedLoanFacility/Created`) [asyncapi:SyndicatedLoan.yaml:11]
- **Other domains named in this purpose text:** Customer Offer [SyndicatedLoan.yaml:4]

## System Development

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/SystemDevelopment.yaml` (sha256 `9671dffd7422…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: SystemDevelopment.yaml`
- **Purpose (verbatim from spec):** Develop new, enhance existing applications and integrate package based systems solutions [SystemDevelopment.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`System` in title) [SystemDevelopment.yaml:3]
- **Control Record:** ITSystemDevelopment [SystemDevelopment.yaml:15]
- **Behavior Qualifiers (5):** FunctionalSpecification [SystemDevelopment.yaml:167], TechnicalSpecification [SystemDevelopment.yaml:300], SoftwareandDataSpecification [SystemDevelopment.yaml:433], TestingSpecification [SystemDevelopment.yaml:566], UsageSpecification [SystemDevelopment.yaml:672]
- **Operations (31):** Capture 5, Control 1, Create 1, Exchange 6, Request 6, Retrieve 6, Update 6 [SystemDevelopment.yaml:12]
- **Schemas:** 20 total, 6 domain-specific, 14 shared-across-≥10-specs
- **Event channels:** 12 (e.g. `ITSystemDevelopment/Created`) [asyncapi:SystemDevelopment.yaml:9]

## Systems Administration

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/SystemsAdministration.yaml` (sha256 `4d4de9ac5780…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: SystemsAdministration.yaml`
- **Purpose (verbatim from spec):** Administer the configuration, maintenance, assignment and track usage and status of all IT assets deployed in development and production across the enterprise [SystemsAdministration.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`System` in title); Customer, Sales & Marketing (`product` in description) [SystemsAdministration.yaml:3]
- **Control Record:** ITSystemAdministrativePlan [SystemsAdministration.yaml:15]
- **Behavior Qualifiers (4):** Assurance [SystemsAdministration.yaml:193], CapacityPlanningandResilience [SystemsAdministration.yaml:246], Configuration [SystemsAdministration.yaml:273], Inventory [SystemsAdministration.yaml:300]
- **Operations (24):** Capture 5, Control 1, Exchange 1, Grant 1, Initiate 1, Request 5, Retrieve 5, Update 5 [SystemsAdministration.yaml:12]
- **Schemas:** 71 total, 8 domain-specific, 63 shared-across-≥10-specs
- **Event channels:** 12 (e.g. `ITSystemAdministrativePlan/Created`) [asyncapi:SystemsAdministration.yaml:10]

## Term Deposit

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/TermDeposit.yaml` (sha256 `404ef62b8c90…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: TermDeposit.yaml`
- **Purpose (verbatim from spec):** A Term Deposit is an interest bearing account into which a customer can place a fixed amount of funds for a fixed amount of time. The Service Domain handles the opening, servicing and maturity processing of a Term Deposit. [TermDeposit.yaml:4]
- **Theme [derived-rule]:** primary Deposits & Accounts; all matches: Deposits & Accounts (`Deposit` in title); Securities, Trading & Markets (`funds` in description); Customer, Sales & Marketing (`customer` in description); Channels & Servicing (`servicing` in description); Corporate Operations & Support (`Service` in description) [TermDeposit.yaml:3]
- **Control Record:** TermDepositFacility [TermDeposit.yaml:15]
- **Behavior Qualifiers (10):** Interest [TermDeposit.yaml:115], Charge [TermDeposit.yaml:140], Sweep [TermDeposit.yaml:218], DebitandCredit [TermDeposit.yaml:323], Payments [TermDeposit.yaml:428], IssuedDevice [TermDeposit.yaml:560], Booking [TermDeposit.yaml:692], Rollover [TermDeposit.yaml:719], AmountBlock [TermDeposit.yaml:746], Deposit [TermDeposit.yaml:824]
- **Operations (35):** Control 1, Exchange 1, Execute 7, Initiate 8, Retrieve 9, Update 9 [TermDeposit.yaml:12]
- **Schemas:** 257 total, 41 domain-specific, 216 shared-across-≥10-specs
- **Event channels:** 22 (e.g. `TermDepositFacility/Created`) [asyncapi:TermDeposit.yaml:11]

## Term Deposit Framework Agreement

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/TermDepositFrameworkAgreement.yaml` (sha256 `89d42f602ad4…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: TermDepositFrameworkAgreement.yaml`
- **Purpose (verbatim from spec):** A Term Deposit Framework Agreement is an agreement between a customer and the bank under which individual term deposits can be opened. It specifies standard conditions that will apply to each underlying term deposit. [TermDepositFrameworkAgreement.yaml:4]
- **Theme [derived-rule]:** primary Deposits & Accounts; all matches: Deposits & Accounts (`Deposit` in title); Customer, Sales & Marketing (`customer` in description); Corporate Operations & Support (`It` in description) [TermDepositFrameworkAgreement.yaml:3]
- **Control Record:** TermDepositFrameworkAgreementFacility [TermDepositFrameworkAgreement.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (3):** Initiate 1, Retrieve 1, Update 1 [TermDepositFrameworkAgreement.yaml:12]
- **Schemas:** 113 total, 2 domain-specific, 111 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `TermDepositFrameworkAgreementFacility/Created`) [asyncapi:TermDepositFrameworkAgreement.yaml:11]
- **Other domains named in this purpose text:** Term Deposit [TermDepositFrameworkAgreement.yaml:4]

## Trade Clearing

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/TradeClearing.yaml` (sha256 `e564728937e0…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: TradeClearing.yaml`
- **Purpose (verbatim from spec):** This Service Domain handles the back office processes that confirm and notify interested parties that securities and funds are available as traded in anticipation of settlement processing [TradeClearing.yaml:4]
- **Theme [derived-rule]:** primary Payments & Settlement; all matches: Payments & Settlement (`Clearing` in title); Securities, Trading & Markets (`securit` in description); Corporate Operations & Support (`Service` in description) [TradeClearing.yaml:3]
- **Control Record:** TradeClearingProcedure [TradeClearing.yaml:15]
- **Behavior Qualifiers (5):** MarketTradeConfirmation [TradeClearing.yaml:217], MarketTradeFundsandSecurityAvailabilityAssurance [TradeClearing.yaml:244], MarketTradeMatching [TradeClearing.yaml:271], MarketTradeOutTradeResolution [TradeClearing.yaml:325], MarketTradeSettlementInitiation [TradeClearing.yaml:352]
- **Operations (43):** Control 1, Exchange 6, Execute 6, Initiate 6, Notify 6, Request 6, Retrieve 6, Update 6 [TradeClearing.yaml:12]
- **Schemas:** 78 total, 7 domain-specific, 71 shared-across-≥10-specs
- **Event channels:** 20 (e.g. `TradeClearingProcedure/Created`) [asyncapi:TradeClearing.yaml:11]

## Trade Confirmation Matching

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/TradeConfirmationMatching.yaml` (sha256 `2e67320beafb…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: TradeConfirmationMatching.yaml`
- **Purpose (verbatim from spec):** This Service Domain supports the bank's interface to a central market matching and confirmation service whether the bank acts as broker dealer or institutional investor [TradeConfirmationMatching.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`market` in description); Corporate Operations & Support (`Service` in description) [TradeConfirmationMatching.yaml:4]
- **Control Record:** TradeMatchingOperatingSession [TradeConfirmationMatching.yaml:15]
- **Behavior Qualifiers (3):** TransactionConfirmationAffirmation [TradeConfirmationMatching.yaml:217], UnmatchedMarketTradeEscalation [TradeConfirmationMatching.yaml:244], TransactionReporting [TradeConfirmationMatching.yaml:298]
- **Operations (29):** Control 1, Exchange 4, Execute 4, Initiate 4, Notify 4, Request 4, Retrieve 4, Update 4 [TradeConfirmationMatching.yaml:12]
- **Schemas:** 35 total, 5 domain-specific, 30 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `TradeMatchingOperatingSession/Created`) [asyncapi:TradeConfirmationMatching.yaml:10]

## Trade Settlement

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/TradeSettlement.yaml` (sha256 `f7a1e7e57f67…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: TradeSettlement.yaml`
- **Purpose (verbatim from spec):** This Service Domain handles the final movement of cash and securities between depositories as previously confirmed in the clearing process, in order to settle a market trade [TradeSettlement.yaml:4]
- **Theme [derived-rule]:** primary Payments & Settlement; all matches: Payments & Settlement (`Settle` in title); Securities, Trading & Markets (`securit` in description); Deposits & Accounts (`deposit` in description); Finance, Accounting & Treasury (`cash` in description); Corporate Operations & Support (`Service` in description) [TradeSettlement.yaml:3]
- **Control Record:** TradeSettlementProcedure [TradeSettlement.yaml:15]
- **Behavior Qualifiers (3):** MarketTradeCashSettlement [TradeSettlement.yaml:167], MarketTradeSettlementConfirmation [TradeSettlement.yaml:194], MarketTradeSecuritiesSettlement [TradeSettlement.yaml:323]
- **Operations (29):** Control 1, Exchange 4, Execute 4, Initiate 4, Notify 4, Request 4, Retrieve 4, Update 4 [TradeSettlement.yaml:12]
- **Schemas:** 76 total, 5 domain-specific, 71 shared-across-≥10-specs
- **Event channels:** 14 (e.g. `TradeSettlementProcedure/Created`) [asyncapi:TradeSettlement.yaml:10]

## Trade and Price Reporting

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/TradeandPriceReporting.yaml` (sha256 `bb4649ceb964…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: TradeandPriceReporting.yaml`
- **Purpose (verbatim from spec):** This Service Domain operates an automated facility that reports executed market trades to the market place as required by the rules of market participation [TradeandPriceReporting.yaml:4]
- **Theme [derived-rule]:** primary Reference & Data Management; all matches: Reference & Data Management (`Report` in title); Securities, Trading & Markets (`market` in description); Corporate Operations & Support (`Service` in description) [TradeandPriceReporting.yaml:3]
- **Control Record:** MarketTradeReportingOperatingSession [TradeandPriceReporting.yaml:15]
- **Behavior Qualifiers (1):** TransactionReporting [TradeandPriceReporting.yaml:217]
- **Operations (15):** Control 1, Exchange 2, Execute 2, Initiate 2, Notify 2, Request 2, Retrieve 2, Update 2 [TradeandPriceReporting.yaml:12]
- **Schemas:** 33 total, 3 domain-specific, 30 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `MarketTradeReportingOperatingSession/Created`) [asyncapi:TradeandPriceReporting.yaml:10]

## Trader Position Operations

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/TraderPositionOperations.yaml` (sha256 `3f262dcccef1…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: TraderPositionOperations.yaml`
- **Purpose (verbatim from spec):** This Service Domain supports the activities of individual traders working within a trading book group [TraderPositionOperations.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Trader` in title); Corporate Operations & Support (`Service` in description) [TraderPositionOperations.yaml:3]
- **Control Record:** TradedPositionOperatingSession [TraderPositionOperations.yaml:15]
- **Behavior Qualifiers (5):** TradeCaptureandReporting [TraderPositionOperations.yaml:217], TradeDealBlotter [TraderPositionOperations.yaml:244], TradeQuoteandPricing [TraderPositionOperations.yaml:271], TraderSecurityPositionManagementandAnalysis [TraderPositionOperations.yaml:298], TraderTradingPermissionsandLimits [TraderPositionOperations.yaml:325]
- **Operations (43):** Control 1, Exchange 6, Execute 6, Initiate 6, Notify 6, Request 6, Retrieve 6, Update 6 [TraderPositionOperations.yaml:12]
- **Schemas:** 37 total, 7 domain-specific, 30 shared-across-≥10-specs
- **Event channels:** 20 (e.g. `TradedPositionOperatingSession/Created`) [asyncapi:TraderPositionOperations.yaml:10]

## Trading Book Oversight

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/TradingBookOversight.yaml` (sha256 `669cddc42eb8…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: TradingBookOversight.yaml`
- **Purpose (verbatim from spec):** This Service Domain oversees the bank's trading book (a type of account ledger that records details of frequently traded securities held by the bank) to manage the banks market risk [TradingBookOversight.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Trading` in title); Risk, Compliance & Fraud (`risk` in description); Deposits & Accounts (`account` in description); Finance, Accounting & Treasury (`ledger` in description); Corporate Operations & Support (`Service` in description) [TradingBookOversight.yaml:3]
- **Control Record:** TradingPositionManagementPlan [TradingBookOversight.yaml:15]
- **Behavior Qualifiers (2):** TradingBookAnalysisandReporting [TradingBookOversight.yaml:91], TradingBookRiskMitigation [TradingBookOversight.yaml:118]
- **Operations (20):** Control 1, Create 1, Exchange 3, Grant 3, Notify 3, Request 3, Retrieve 3, Update 3 [TradingBookOversight.yaml:12]
- **Schemas:** 70 total, 7 domain-specific, 63 shared-across-≥10-specs
- **Event channels:** 11 (e.g. `TradingPositionManagementPlan/Created`) [asyncapi:TradingBookOversight.yaml:11]

## Transaction Authorization

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/TransactionAuthorization.yaml` (sha256 `45c8b370304a…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: TransactionAuthorization.yaml`
- **Purpose (verbatim from spec):** This service domain handles risk based authorization for interactive customer transactions. This combines the context (channel) transaction, customer details and recent activity analysis as appropriate. The authorization may require a specific level of party/customer authentication to get approval. [TransactionAuthorization.yaml:4]
- **Theme [derived-rule]:** primary Risk, Compliance & Fraud; all matches: Risk, Compliance & Fraud (`risk` in description); Customer, Sales & Marketing (`customer` in description); Channels & Servicing (`channel` in description); Corporate Operations & Support (`service` in description) [TransactionAuthorization.yaml:4]
- **Control Record:** InteractiveTransactionAssessment [TransactionAuthorization.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (7):** Evaluate 1, Exchange 1, Execute 1, Grant 1, Request 1, Retrieve 1, Update 1 [TransactionAuthorization.yaml:12]
- **Schemas:** 65 total, 6 domain-specific, 59 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `InteractiveTransactionAssessment/Created`) [asyncapi:TransactionAuthorization.yaml:12]

## Transaction Engine

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/TransactionEngine.yaml` (sha256 `0be87f78ea67…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: TransactionEngine.yaml`
- **Purpose (verbatim from spec):** Orchestrate a schedule of payment transaction and reporting activities for the fulfillment of certain long term instruments or structured facilities [TransactionEngine.yaml:4]
- **Theme [derived-rule]:** primary Payments & Settlement; all matches: Payments & Settlement (`payment` in description); Reference & Data Management (`report` in description); Corporate Operations & Support (`facilit` in description) [TransactionEngine.yaml:4]
- **Control Record:** TransactionScheduleFacility [TransactionEngine.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (6):** Control 1, Exchange 1, Execute 1, Initiate 1, Retrieve 1, Update 1 [TransactionEngine.yaml:12]
- **Schemas:** 105 total, 1 domain-specific, 104 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `TransactionScheduleFacility/Created`) [asyncapi:TransactionEngine.yaml:10]

## Trust Services

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/TrustServices.yaml` (sha256 `077188187834…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: TrustServices.yaml`
- **Purpose (verbatim from spec):** This Service Domain support a range of trust management services offered to high value customers [TrustServices.yaml:4]
- **Theme [derived-rule]:** primary Corporate Operations & Support; all matches: Corporate Operations & Support (`Service` in title); Customer, Sales & Marketing (`customer` in description) [TrustServices.yaml:3]
- **Control Record:** CorporateTrustServicesFacility [TrustServices.yaml:15]
- **Behavior Qualifiers (2):** CourtLiaison [TrustServices.yaml:217], LoanAgencyandAdministration [TrustServices.yaml:244]
- **Operations (22):** Control 1, Exchange 3, Execute 3, Initiate 3, Notify 3, Request 3, Retrieve 3, Update 3 [TrustServices.yaml:12]
- **Schemas:** 124 total, 4 domain-specific, 120 shared-across-≥10-specs
- **Event channels:** 11 (e.g. `CorporateTrustServicesFacility/Created`) [asyncapi:TrustServices.yaml:9]

## Underwriting

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/Underwriting.yaml` (sha256 `861885e79152…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: Underwriting.yaml`
- **Purpose (verbatim from spec):** This service domain manages the underwriting decision process for products as appropriate (including many loan types and some insurance products) [Underwriting.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Underwrit` in title); Lending & Credit (`loan` in description); Customer, Sales & Marketing (`product` in description); Corporate Operations & Support (`service` in description) [Underwriting.yaml:3]
- **Control Record:** UnderwritingAssessment [Underwriting.yaml:15]
- **Behavior Qualifiers:** none
- **Operations (7):** Evaluate 1, Exchange 1, Execute 1, Grant 1, Request 1, Retrieve 1, Update 1 [Underwriting.yaml:12]
- **Schemas:** 79 total, 10 domain-specific, 69 shared-across-≥10-specs
- **Event channels:** 2 (e.g. `UnderwritingAssessment/Created`) [asyncapi:Underwriting.yaml:10]

## Unit Trust Administration

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/UnitTrustAdministration.yaml` (sha256 `db2ddb27d408…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: UnitTrustAdministration.yaml`
- **Purpose (verbatim from spec):** This Service Domain handles the implementation and fulfillment of unit investment trusts [UnitTrustAdministration.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`investment` in description); Corporate Operations & Support (`Service` in description) [UnitTrustAdministration.yaml:4]
- **Control Record:** UnitTrustAdministrativePlan [UnitTrustAdministration.yaml:15]
- **Behavior Qualifiers (6):** FundAccounting [UnitTrustAdministration.yaml:217], FundInvestor_MiddleandBackOfficeService [UnitTrustAdministration.yaml:244], FundEnrolment [UnitTrustAdministration.yaml:271], FundFinancialReporting [UnitTrustAdministration.yaml:298], FundManagementFee [UnitTrustAdministration.yaml:325], FundTaxAdministration [UnitTrustAdministration.yaml:352]
- **Operations (44):** Control 1, Create 1, Exchange 7, Grant 7, Notify 7, Request 7, Retrieve 7, Update 7 [UnitTrustAdministration.yaml:12]
- **Schemas:** 71 total, 9 domain-specific, 62 shared-across-≥10-specs
- **Event channels:** 23 (e.g. `UnitTrustAdministrativePlan/Created`) [asyncapi:UnitTrustAdministration.yaml:9]

## Virtual Account

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/VirtualAccount.yaml` (sha256 `9d915aa96d83…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: VirtualAccount.yaml`
- **Purpose (verbatim from spec):** A Virtual Account is a bank account that is defined on an underlying real account. It can receive and send payments for the underlying account while behaving towards the outside as a separate account. [VirtualAccount.yaml:4]
- **Theme [derived-rule]:** primary Deposits & Accounts; all matches: Deposits & Accounts (`Account` in title); Payments & Settlement (`payment` in description); Corporate Operations & Support (`It` in description) [VirtualAccount.yaml:3]
- **Control Record:** VirtualAccountFacility [VirtualAccount.yaml:15]
- **Behavior Qualifiers (8):** DirectDebit [VirtualAccount.yaml:245], Payment [VirtualAccount.yaml:272], Charge [VirtualAccount.yaml:326], Interest [VirtualAccount.yaml:380], FinancialStatusTracking [VirtualAccount.yaml:881], AmountBlock [VirtualAccount.yaml:935], IssuedDevice [VirtualAccount.yaml:1013], Booking [VirtualAccount.yaml:1091]
- **Operations (42):** Capture 3, Control 2, Exchange 3, Execute 5, Grant 3, Initiate 7, Request 5, Retrieve 7, Update 7 [VirtualAccount.yaml:12]
- **Schemas:** 218 total, 26 domain-specific, 192 shared-across-≥10-specs
- **Event channels:** 24 (e.g. `VirtualAccountFacility/Created`) [asyncapi:VirtualAccount.yaml:11]

## eBranch Management

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/eBranchManagement.yaml` (sha256 `6029136c1dba…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: eBranchManagement.yaml`
- **Purpose (verbatim from spec):** Oversee the configuration and operation of the e-branch channel facilities [eBranchManagement.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Branch` in title); Corporate Operations & Support (`facilit` in description) [eBranchManagement.yaml:3]
- **Control Record:** eBranchChannelManagementPlan [eBranchManagement.yaml:15]
- **Behavior Qualifiers (3):** MaintenanceAndUpgrades [eBranchManagement.yaml:141], CapacityPlanning [eBranchManagement.yaml:168], Troubleshooting [eBranchManagement.yaml:300]
- **Operations (15):** Create 2, Exchange 1, Request 4, Retrieve 4, Update 4 [eBranchManagement.yaml:12]
- **Schemas:** 35 total, 5 domain-specific, 30 shared-across-≥10-specs
- **Event channels:** 8 (e.g. `eBranchChannelManagementPlan/Created`) [asyncapi:eBranchManagement.yaml:9]

## eBranch Operations

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/eBranchOperations.yaml` (sha256 `968473e9706b…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: eBranchOperations.yaml`
- **Purpose (verbatim from spec):** This service domain operates the bank's on-line web based electronic branch capabilities - controlling access and load balancing across available communications and processing resources to optimize performance/availability [eBranchOperations.yaml:4]
- **Theme [derived-rule]:** primary Channels & Servicing; all matches: Channels & Servicing (`Branch` in title); Corporate Operations & Support (`service` in description) [eBranchOperations.yaml:3]
- **Control Record:** eBranchChannelOperatingSession [eBranchOperations.yaml:15]
- **Behavior Qualifiers (2):** Inbound [eBranchOperations.yaml:91], Outbound [eBranchOperations.yaml:142]
- **Operations (9):** Control 1, Initiate 3, Request 1, Retrieve 3, Update 1 [eBranchOperations.yaml:12]
- **Schemas:** 48 total, 4 domain-specific, 44 shared-across-≥10-specs
- **Event channels:** 6 (e.g. `eBranchChannelOperatingSession/Created`) [asyncapi:eBranchOperations.yaml:11]

## eTrading Workbench

- **Spec file:** `release14.0.0/semantic-apis/oas3 /yamls/eTradingWorkbench.yaml` (sha256 `9ceae0c34d6f…`, version 14.0.0); bundle: `oas3_yamls_part6.md` under `# FILE: eTradingWorkbench.yaml`
- **Purpose (verbatim from spec):** This Service Domain supports consumer securities trading of their investment portfolio through the bank [eTradingWorkbench.yaml:4]
- **Theme [derived-rule]:** primary Securities, Trading & Markets; all matches: Securities, Trading & Markets (`Trading` in title); Corporate Operations & Support (`Service` in description) [eTradingWorkbench.yaml:3]
- **Control Record:** eTradingWorkbenchOperatingSession [eTradingWorkbench.yaml:15]
- **Behavior Qualifiers (4):** MarketOrderInitiation [eTradingWorkbench.yaml:191], MarketOrderQuotation [eTradingWorkbench.yaml:244], MarketPriceAnalysis [eTradingWorkbench.yaml:271], InvestmentPortfolioValuation [eTradingWorkbench.yaml:298]
- **Operations (36):** Control 1, Exchange 5, Execute 5, Initiate 5, Notify 5, Request 5, Retrieve 5, Update 5 [eTradingWorkbench.yaml:12]
- **Schemas:** 36 total, 6 domain-specific, 30 shared-across-≥10-specs
- **Event channels:** 17 (e.g. `eTradingWorkbenchOperatingSession/Created`) [asyncapi:eTradingWorkbench.yaml:10]
