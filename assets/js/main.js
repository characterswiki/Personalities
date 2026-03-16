/**
 * Personalities Database – Search & UI Enhancements
 * Provides live filtering of character cards based on search input.
 */

document.addEventListener('DOMContentLoaded', function() {
  // ===== SEARCH FUNCTIONALITY =====
  const searchInput = document.getElementById('search');
  const cards = document.querySelectorAll('.card');
  const cardsContainer = document.querySelector('.cards');

  // Create a "no results" message element
  const noResultsMsg = document.createElement('p');
  noResultsMsg.className = 'no-results';
  noResultsMsg.textContent = 'No characters match your search.';
  noResultsMsg.style.display = 'none';
  noResultsMsg.style.textAlign = 'center';
  noResultsMsg.style.padding = '2rem';
  noResultsMsg.style.color = '#718096';
  noResultsMsg.style.fontSize = '1.1rem';
  cardsContainer.parentNode.insertBefore(noResultsMsg, cardsContainer.nextSibling);

  if (searchInput) {
    searchInput.addEventListener('input', function(e) {
      const query = e.target.value.trim().toLowerCase();
      let visibleCount = 0;

      cards.forEach(card => {
        const name = card.querySelector('h2').textContent.toLowerCase();
        const description = card.querySelector('p').textContent.toLowerCase();
        const matches = name.includes(query) || description.includes(query);

        if (matches) {
          card.style.display = 'flex';  // restore original display
          visibleCount++;
        } else {
          card.style.display = 'none';
        }
      });

      // Show/hide no results message
      if (visibleCount === 0) {
        noResultsMsg.style.display = 'block';
      } else {
        noResultsMsg.style.display = 'none';
      }
    });
  }

  // ===== SMOOTH SCROLL FOR INTERNAL LINKS (optional) =====
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href === '#') return;
      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // ===== KEYBOARD SHORTCUT: Focus search with '/' =====
  document.addEventListener('keydown', function(e) {
    if (e.key === '/' && !e.ctrlKey && !e.metaKey && document.activeElement !== searchInput) {
      e.preventDefault();
      searchInput.focus();
    }
  });

  // ===== LAZY LOADING FOR CARD IMAGES (if you add any later) =====
  // (Placeholder for future enhancements)
});
