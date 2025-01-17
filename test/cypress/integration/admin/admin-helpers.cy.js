export class AdminPage {
  login() {
    cy.session(
      'login',
      () => {
        this.open();
        this.submitLoginForm();
      },
      {
        validate() {
          cy.getCookie('sessionid').should('exist');
        },
      },
    );

    this.open();
  }

  open() {
    cy.visit('/admin/');
  }

  submitLoginForm() {
    cy.get('#id_username').type('admin');
    cy.get('#id_password').type('admin');
    cy.get('form').submit();
  }

  successBanner() {
    return cy.get('.messages').find('.success');
  }

  openImageGallery() {
    cy.visit('/admin/images/');
  }

  getImages() {
    return cy.get('#image-results').find('li');
  }

  tags() {
    return cy.get('.tagfilter');
  }

  openDocumentsLibrary() {
    cy.visit('/admin/documents/');
  }

  getFirstDocument() {
    return cy.get('#document-results').find('tr').eq(1);
  }

  openContacts() {
    this.openNavigationTab('Snippets');
    this.selectSubMenu('Contacts');
  }

  addContact() {
    cy.get('a[href="/admin/snippets/v1/contact/add/"]:first').click();
    cy.get('#id_heading').type('Test heading');
    cy.get('.DraftEditor-root').type('Random Body');
    this.submitForm();
  }

  searchContact(contact_heading) {
    cy.get('#id_q').type(contact_heading);
    cy.get('#id_q').type('{enter}');
  }

  removeContact() {
    cy.get('a[href^="/admin/snippets/v1/contact/delete/"]:first').click({
      force: true,
    });
    cy.get('[value="Yes, delete"]').click();
  }

  addMortgageData(name) {
    cy.get(
      `a[href="/admin/snippets/data_research/mortgage${name}/add/"]:first`,
    ).click();
    cy.get('#id_name').type('test');
    this.submitForm();
  }

  openMortgageData(name) {
    this.openNavigationTab('Data Research');
    this.selectSubMenu(`Mortgage ${name}`);
  }

  openNavigationTab(name) {
    cy.get('.sidebar-menu-item').contains(name).click();
  }

  selectSubMenu(name) {
    cy.get('.sidebar-menu-item--in-sub-menu').contains(name).click();
  }

  openRegulations() {
    this.openNavigationTab('Regulations');
  }

  editRegulation() {
    this.getFirstTableRow().trigger('mouseover');
    cy.get('a[href^="/admin/regulations3k/part/edit/"]:first').click({
      force: true,
    });
    this.submitForm();
  }

  copyRegulation() {
    this.getFirstTableRow().find('.children').click();
    this.getFirstTableRow().contains('Copy').click({ force: true });
    this.setRegulationEffectiveDate('3099-01-01');
    this.submitForm();
  }

  cleanUpRegulations() {
    cy.get('table tr').last().contains('Delete').click({ force: true });
    this.submitForm();
  }

  setRegulationEffectiveDate(name) {
    cy.get('#id_effective_date').clear();
    cy.get('#id_effective_date').type(name);
  }

  openMegaMenu() {
    this.openNavigationTab('Mega menu');
  }

  editMegaMenu() {
    this.getFirstTableRow().contains('Edit').click({ force: true });
    this.submitForm();
  }

  openBuildingBlockActivity() {
    this.openNavigationTab('TDP Activity');
    this.selectSubMenu('Building Block');
  }

  editBuildingBlock() {
    this.getFirstTableRow().contains('Edit').click({ force: true });
    this.submitForm();
  }

  openApplicantTypes() {
    this.openNavigationTab('Job listings');
    this.selectSubMenu('Applicant types');
  }

  editApplicantType() {
    this.getFirstTableRow().contains('Edit').click({ force: true });
    this.submitForm();
  }

  openFlag() {
    this.openNavigationTab('Settings');
    this.selectSubMenu('Flags');
    this.getFirstTableRow().find('a').first().click();
  }

  toggleFlag() {
    cy.get('.flag > a').first().click();
  }

  flagHeading() {
    return cy.get('.help-block');
  }

  openBlockInventory() {
    this.openNavigationTab('Reports');
    this.selectSubMenu('Block Inventory');
  }

  searchResults() {
    return cy.get('.listing');
  }

  searchExternalLink(link) {
    cy.get('#id_url').type(link);
    this.submitForm();
  }

  openDjangoAdmin() {
    this.openNavigationTab('Django Admin');
  }

  submitForm() {
    cy.get('main form[method="POST"]').submit();
  }

  getFirstTableRow() {
    return cy.get('.listing tr').eq(1);
  }

  getPageMetadataReports() {
    this.openNavigationTab('Reports');
    this.selectSubMenu('Page Metadata');
    return cy.get('.listing').find('tr');
  }

  addSublandingPage() {
    cy.visit('/admin/pages/add/v1/sublandingpage/1/');
    cy.url().should('include', 'sublandingpage');
  }

  clickBlock(name) {
    const addBlockButton = cy.get(
      'div[data-contentpath="content"] .c-sf-add-button',
    );
    addBlockButton.should('be.visible');
    addBlockButton.click();

    const addTableOption = cy.contains('div.w-combobox__option', name);
    addTableOption.should('be.visible');
    return addTableOption.click();
  }

  addTable() {
    cy.get('input[value="table"]', { timeout: 1000 }).should('not.exist');
    this.clickBlock('Table');
    cy.get('input[value="table"]', { timeout: 1000 }).should('exist');
  }

  setClipboard(text) {
    cy.window().its('navigator.clipboard').invoke('writeText', text);
  }

  getTableHeadingCell() {
    return cy.get('input[name="content-0-value-data-column-0-heading"]');
  }

  getTableDataCell() {
    return cy.get('input[name="content-0-value-data-cell-0-1"]');
  }

  getTableData() {
    return '00\t01\n10\t11\n';
  }

  pasteTableAsText() {
    cy.get('button.paste-as-text').click();
  }

  pasteTableAsRichText() {
    cy.get('button.paste-as-rich-text').click();
  }
}
