const initMeclix = () => {

  /* ==========================================================================
     1. ACTIVE PAGE HEADER LINK NAVIGATION
     ========================================================================== */
  const path = window.location.pathname;
  let pageName = path.split('/').pop();
  if (pageName === '' || !pageName) {
    pageName = 'index.html';
  }

  const navLinks = document.querySelectorAll('.nav-link');
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    // Match exact filename or map root/index
    if (pageName === href || (pageName === 'index.html' && href === 'index.html')) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });

  /* ==========================================================================
     2. GLOBAL HEADER SCROLL EFFECT
     ========================================================================== */
  const header = document.getElementById('site-header') || document.getElementById('masthead') || document.querySelector('.site-header');
  window.addEventListener('scroll', () => {
    if (header) {
      if (window.scrollY > 40) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }
  });

  /* ==========================================================================
     3. MOBILE NAVIGATION DRAWER
     ========================================================================== */
  const menuToggle = document.getElementById('menu-toggle');
  const navMenu = document.getElementById('nav-menu');

  if (menuToggle && navMenu) {
    menuToggle.addEventListener('click', () => {
      navMenu.classList.toggle('mobile-open');
    });
  }

  /* ==========================================================================
     4. LANDING PRODUCTS TABS CONTROLLER (Only on Home Page)
     ========================================================================== */
  const tabButtons = document.querySelectorAll('.product-tabs-wrapper .tab-btn');
  const tabPanes = document.querySelectorAll('.product-tabs-wrapper .tab-pane');

  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetTabId = btn.getAttribute('data-tab');
      
      tabButtons.forEach(b => b.classList.remove('active'));
      tabPanes.forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      const targetPane = document.getElementById(targetTabId);
      if (targetPane) {
        targetPane.classList.add('active');
      }
    });
  });

  /* ==========================================================================
     5. STAKEHOLDER MATRIX ROW FILTER (Only on Smart Locker Page)
     ========================================================================== */
  const matrixFilterBtns = document.querySelectorAll('#stakeholder-filters .matrix-btn');
  const matrixRows = document.querySelectorAll('#stakeholder-matrix-body tr');

  matrixFilterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const filterGroup = btn.getAttribute('data-stakeholder');
      
      matrixFilterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      matrixRows.forEach(row => {
        const rowGroups = row.getAttribute('data-groups');
        if (filterGroup === 'all' || rowGroups === filterGroup) {
          row.style.display = 'table-row';
        } else {
          row.style.display = 'none';
        }
      });
    });
  });

  /* ==========================================================================
     6. KEY USE CASES TABS SWITCHER (Only on KeyKnox Page)
     ========================================================================== */
  const keyUsecaseBtns = document.querySelectorAll('#key-usecase-nav button');
  const keyUsecasePanes = document.querySelectorAll('.use-case-tab-content .use-case-pane');

  keyUsecaseBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-keyuse');
      
      keyUsecaseBtns.forEach(b => b.classList.remove('active'));
      keyUsecasePanes.forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      const targetPane = document.getElementById(`key-usecase-${targetId}`);
      if (targetPane) {
        targetPane.classList.add('active');
      }
    });
  });

  /* ==========================================================================
     7. TECHNICAL SPECIFICATIONS TABS SWITCHER (Only on Software Page)
     ========================================================================== */
  const specTabBtns = document.querySelectorAll('#specs-panel-nav button');
  const specPanes = document.querySelectorAll('.specs-panes .specs-pane');

  specTabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-spec');
      
      specTabBtns.forEach(b => b.classList.remove('active'));
      specPanes.forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      const targetPane = document.getElementById(`spec-sheet-${targetId}`);
      if (targetPane) {
        targetPane.classList.add('active');
      }
    });
  });

  /* ==========================================================================
     8. CONSULTATION MODAL DIALOG CONTROLS
     ========================================================================== */
  const consultationModal = document.getElementById('consultation-modal');
  const modalCloseBtn = document.getElementById('modal-close-btn');
  const successDoneBtn = document.getElementById('success-done-btn');
  const bookingFormContainer = document.getElementById('booking-form-container');
  const bookingSuccessContainer = document.getElementById('booking-success-container');
  const consultationForm = document.getElementById('consultation-form');

  // Open modal on triggers - direct attachment for bulletproof execution
  const bindTriggers = () => {
    const triggers = document.querySelectorAll('.btn-consultation-trigger');
    triggers.forEach(trigger => {
      trigger.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        if (consultationModal) consultationModal.classList.add('open');
        if (bookingFormContainer) bookingFormContainer.style.display = 'block';
        if (bookingSuccessContainer) bookingSuccessContainer.style.display = 'none';
        if (consultationForm) consultationForm.reset();
        
        const bookingDateEl = document.getElementById('booking-date');
        if (bookingDateEl) {
          const tomorrow = new Date();
          tomorrow.setDate(tomorrow.getDate() + 1);
          const tomorrowStr = tomorrow.toISOString().split('T')[0];
          bookingDateEl.value = tomorrowStr;
          bookingDateEl.min = tomorrowStr;
        }
      });
    });
  };
  bindTriggers();

  // Document-level fallback trigger
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('.btn-consultation-trigger');
    if (trigger) {
      e.preventDefault();
      if (consultationModal) consultationModal.classList.add('open');
      if (bookingFormContainer) bookingFormContainer.style.display = 'block';
      if (bookingSuccessContainer) bookingSuccessContainer.style.display = 'none';
      if (consultationForm) consultationForm.reset();
      
      // Set default preferred date to tomorrow if element exists
      const bookingDateEl = document.getElementById('booking-date');
      if (bookingDateEl) {
        const tomorrow = new Date();
        tomorrow.setDate(tomorrow.getDate() + 1);
        const tomorrowStr = tomorrow.toISOString().split('T')[0];
        bookingDateEl.value = tomorrowStr;
        bookingDateEl.min = tomorrowStr;
      }
    }
  });

  // Close modal functions
  function closeModal() {
    if (consultationModal) consultationModal.classList.remove('open');
  }

  if (modalCloseBtn) modalCloseBtn.addEventListener('click', closeModal);
  if (successDoneBtn) successDoneBtn.addEventListener('click', closeModal);
  
  // Close on backdrop click
  if (consultationModal) {
    consultationModal.addEventListener('click', (e) => {
      if (e.target === consultationModal) {
        closeModal();
      }
    });
  }

  // Submit Logic
  if (consultationForm) {
    consultationForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      // Custom Validation Checks
      let isValid = true;
      const inputs = consultationForm.querySelectorAll('.modal-form-input, .form-input');
      
      inputs.forEach(input => {
        if (!input.checkValidity()) {
          isValid = false;
          input.style.borderColor = '#ff5f56';
        } else {
          input.style.borderColor = 'var(--border-light)';
        }
      });

      if (isValid) {
        // Simulate API submit delay
        const submitBtn = document.getElementById('booking-submit-btn');
        if (submitBtn) {
          submitBtn.textContent = 'Scheduling Slot...';
          submitBtn.disabled = true;
        }

        setTimeout(() => {
          if (bookingFormContainer) bookingFormContainer.style.display = 'none';
          if (bookingSuccessContainer) bookingSuccessContainer.style.display = 'block';
          if (submitBtn) {
            submitBtn.textContent = 'Book Consultation Session';
            submitBtn.disabled = false;
          }
          consultationForm.reset();
        }, 1000);
      }
    });
  }

  /* ==========================================================================
     9. HERO CABINET INTERACTIVE EVENT SIMULATOR (Only on Home Page)
     ========================================================================== */
  const simHooks = document.querySelectorAll('.cabinet-sim .key-hook');
  const simEventsList = document.getElementById('sim-events-list');
  
  const simUserNames = ['Rohan Sharma', 'Vikram Singh', 'Priya Patil', 'Aditya Iyer', 'Neha Verma'];
  
  function addSimulatedLog(message) {
    const time = new Date();
    const hrs = String(time.getHours()).padStart(2, '0');
    const mins = String(time.getMinutes()).padStart(2, '0');
    const secs = String(time.getSeconds()).padStart(2, '0');
    
    const logLine = document.createElement('div');
    logLine.className = 'sim-event-line';
    logLine.innerHTML = `> <span class="cyan">${hrs}:${mins}:${secs}</span> ${message}`;
    
    simEventsList.appendChild(logLine);
    
    // Auto Scroll simulated terminal
    if (simEventsList.childNodes.length > 5) {
      simEventsList.removeChild(simEventsList.firstChild);
    }
  }

  // Simulation loop changing key cabinet hook states
  if (simHooks.length > 0 && simEventsList) {
    setInterval(() => {
      // Select a random hook to change status
      const randIndex = Math.floor(Math.random() * simHooks.length);
      const hook = simHooks[randIndex];
      
      if (hook.classList.contains('active-key')) {
        const isKeyIn = hook.classList.contains('in');
        const userName = simUserNames[Math.floor(Math.random() * simUserNames.length)];
        const keyNum = randIndex + 1;
        
        if (isKeyIn) {
          // Take Key OUT
          hook.classList.remove('in');
          hook.classList.add('out');
          addSimulatedLog(`Key #0${keyNum} <span class="red">OUT</span> by ${userName}`);
        } else {
          // Return Key IN
          hook.classList.remove('out');
          hook.classList.add('in');
          addSimulatedLog(`Key #0${keyNum} <span class="green">IN</span> by ${userName}`);
        }
      }
    }, 4000);
  }

};

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initMeclix);
} else {
  initMeclix();
}
