<template>
  <div>
    <h2>Все заимствованные книги</h2>
    <ul>
      <li v-for="book in borrowedBooks" :key="book.id" :class="{ 'overdue': book.is_overdue }">
        <p>
          <a :href="`/book-detail/${book.book}`">{{ book.title }}</a>
          - {{ book.borrower }}
          <br>
          Дата возврата: {{ formatDate(book.due_back) }}
        </p>
      </li>
    </ul>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  name: 'BorrowedBooksPage',
  setup() {
    const borrowedBooks = ref([]);
    const fetchBorrowedBooks = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/accounts/all_borrower/', {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`,
          },
        });
        borrowedBooks.value = response.data;
        console.log(borrowedBooks.value)
      } catch (error) {
        console.error('Ошибка при загрузке заимствованных книг:', error);
      }
    };

    onMounted(() => {
      fetchBorrowedBooks();
    });

    const formatDate = (date) => {
      // Преобразуем дату в удобный формат
      const options = {year: 'numeric', month: 'long', day: 'numeric'};
      return new Date(date).toLocaleDateString('ru-RU', options);
    };

    return {
      borrowedBooks,
      formatDate,
    };
  },
};
</script>

<style scoped>
h2 {
  color: #333;
}

.overdue {
  color: red; /* Выделение просроченных книг */
}
</style>
