### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">29.72</td>
    <td align="right">17.29</td>
    <td align="right">6.29</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">13.07</td>
    <td align="right">12.40</td>
    <td align="right">17.42</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.79</td>
    <td align="right">4.96</td>
    <td align="right">5.05</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.08</td>
    <td align="right">6.86</td>
    <td align="right">6.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">19.22</td>
    <td align="right">17.95</td>
    <td align="right">17.90</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.46</td>
    <td align="right">5.41</td>
    <td align="right">5.41</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.67</td>
    <td align="right">9.49</td>
    <td align="right">9.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">24.66</td>
    <td align="right">22.92</td>
    <td align="right">17.34</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.21</td>
    <td align="right">6.06</td>
    <td align="right">6.30</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.48</td>
    <td align="right">14.59</td>
    <td align="right">14.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">35.42</td>
    <td align="right">33.26</td>
    <td align="right">18.06</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">7.77</td>
    <td align="right">7.78</td>
    <td align="right">7.61</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">15.18</td>
    <td align="right">18.52</td>
    <td align="right">18.65</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7269</td>
    <td align="right">8.17</td>
    <td align="right">10.68</td>
    <td align="right">10.73</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.69</td>
    <td align="right">5.82</td>
    <td align="right">5.83</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.25</td>
    <td align="right">6.64</td>
    <td align="right">6.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">4.26</td>
    <td align="right">5.36</td>
    <td align="right">5.36</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.07</td>
    <td align="right">6.07</td>
    <td align="right">6.09</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">12.71</td>
    <td align="right">9.86</td>
    <td align="right">9.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">17.89</td>
    <td align="right">11.00</td>
    <td align="right">8.85</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.30</td>
    <td align="right">7.28</td>
    <td align="right">7.33</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">13.03</td>
    <td align="right">13.34</td>
    <td align="right">13.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">11.97</td>
    <td align="right">13.18</td>
    <td align="right">8.33</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.63</td>
    <td align="right">8.71</td>
    <td align="right">8.57</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.49</td>
    <td align="right">17.41</td>
    <td align="right">17.37</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, X64
<!--clang-x64/comparison_table.cpp.txt-->
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.79</td>
    <td align="right">17.11</td>
    <td align="right">6.25</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">11.14</td>
    <td align="right">10.82</td>
    <td align="right">16.50</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.98</td>
    <td align="right">4.64</td>
    <td align="right">4.63</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.99</td>
    <td align="right">7.24</td>
    <td align="right">7.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">14.97</td>
    <td align="right">15.57</td>
    <td align="right">17.59</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.38</td>
    <td align="right">5.04</td>
    <td align="right">5.05</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">9.82</td>
    <td align="right">10.02</td>
    <td align="right">10.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">19.55</td>
    <td align="right">19.56</td>
    <td align="right">16.47</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">5.19</td>
    <td align="right">5.89</td>
    <td align="right">5.92</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.42</td>
    <td align="right">15.09</td>
    <td align="right">15.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">29.67</td>
    <td align="right">29.52</td>
    <td align="right">17.33</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">9.68</td>
    <td align="right">7.85</td>
    <td align="right">12.64</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">16.99</td>
    <td align="right">20.03</td>
    <td align="right">28.50</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7269</td>
    <td align="right">4.33</td>
    <td align="right">5.06</td>
    <td align="right">5.05</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.62</td>
    <td align="right">5.34</td>
    <td align="right">5.33</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.04</td>
    <td align="right">7.18</td>
    <td align="right">7.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">3.36</td>
    <td align="right">4.27</td>
    <td align="right">4.23</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.05</td>
    <td align="right">5.95</td>
    <td align="right">5.87</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.31</td>
    <td align="right">10.42</td>
    <td align="right">10.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">11.07</td>
    <td align="right">7.64</td>
    <td align="right">6.06</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">5.90</td>
    <td align="right">6.85</td>
    <td align="right">7.32</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">12.86</td>
    <td align="right">16.37</td>
    <td align="right">16.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">13.36</td>
    <td align="right">9.66</td>
    <td align="right">6.87</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">7.22</td>
    <td align="right">8.33</td>
    <td align="right">8.23</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.65</td>
    <td align="right">17.66</td>
    <td align="right">17.92</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.98</td>
    <td align="right">14.19</td>
    <td align="right">9.04</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">9.86</td>
    <td align="right">12.28</td>
    <td align="right">20.66</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.67</td>
    <td align="right">4.58</td>
    <td align="right">4.84</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">4.30</td>
    <td align="right">5.45</td>
    <td align="right">4.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">31.77</td>
    <td align="right">30.79</td>
    <td align="right">26.40</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.42</td>
    <td align="right">7.90</td>
    <td align="right">8.25</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">9.97</td>
    <td align="right">10.66</td>
    <td align="right">9.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">54.28</td>
    <td align="right">42.44</td>
    <td align="right">25.42</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">11.32</td>
    <td align="right">9.71</td>
    <td align="right">9.44</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">18.58</td>
    <td align="right">14.96</td>
    <td align="right">14.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">78.12</td>
    <td align="right">58.74</td>
    <td align="right">27.01</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">13.66</td>
    <td align="right">10.62</td>
    <td align="right">11.19</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">22.12</td>
    <td align="right">19.41</td>
    <td align="right">20.87</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">4.69</td>
    <td align="right">6.78</td>
    <td align="right">6.23</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">3.08</td>
    <td align="right">4.32</td>
    <td align="right">3.63</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.86</td>
    <td align="right">4.09</td>
    <td align="right">4.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">6.84</td>
    <td align="right">7.70</td>
    <td align="right">7.62</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.71</td>
    <td align="right">7.56</td>
    <td align="right">7.68</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">10.87</td>
    <td align="right">11.09</td>
    <td align="right">10.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">13.62</td>
    <td align="right">14.64</td>
    <td align="right">10.30</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">15.33</td>
    <td align="right">10.95</td>
    <td align="right">9.89</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">19.18</td>
    <td align="right">15.26</td>
    <td align="right">16.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">14.83</td>
    <td align="right">17.63</td>
    <td align="right">11.11</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.98</td>
    <td align="right">7.78</td>
    <td align="right">7.99</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">18.90</td>
    <td align="right">17.92</td>
    <td align="right">18.12</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->
